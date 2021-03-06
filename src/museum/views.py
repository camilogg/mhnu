from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from weasyprint import HTML

from museum.models import Record


def record_detail_pdf(request, pk):
    record = get_object_or_404(Record, pk=pk)
    response = HttpResponse(content_type='application/pdf')

    # Lo descarga directamente
    # response['Content-Disposition'] = "attachment; filename=certificado.pdf"

    # Lo visualiza
    response['Content-Disposition'] = 'inline; filename=record.pdf'

    html_string = render_to_string('museum/record_detail_pdf.html', {
        'record': record
    })

    HTML(
        string=html_string, base_url=request.build_absolute_uri(),
    ).write_pdf(response, presentational_hints=True)
    return response
    # return render(request, 'museum/record_detail_pdf.html', {
    #     'record': record
    # })


def record_list_pdf(request, queryset):

    response = HttpResponse(content_type='application/pdf')

    # Lo descarga directamente
    # response['Content-Disposition'] = "attachment; filename=certificado.pdf"

    # Lo visualiza
    response['Content-Disposition'] = 'inline; filename=record.pdf'

    html_string = render_to_string('museum/record_list_pdf.html', {
        'records': queryset
    })

    HTML(
        string=html_string, base_url=request.build_absolute_uri(),
    ).write_pdf(response, presentational_hints=True)
    return response
    # return render(request, 'museum/record_list_pdf.html', {
    #     'records': queryset
    # })
