from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from weasyprint import HTML

from museum.models import Record
from museum.utils import django_url_fetcher


def record_detail_pdf(request, pk):
    record = get_object_or_404(Record, pk=pk)
    response = HttpResponse(content_type='application/pdf')

    # Lo descarga directamente
    # response['Content-Disposition'] = "attachment; filename=certificado.pdf"

    # Lo visualiza
    response['Content-Disposition'] = 'inline; filename=record.pdf'

    html_string = render_to_string('museum/record_detail_pdf.html', {
        'record': record,
    })

    HTML(
        string=html_string,
        base_url=settings.HOST_URL,
        url_fetcher=django_url_fetcher
    ).write_pdf(response, presentational_hints=True)
    return response
    # return render(request, 'museum/record_detail_pdf.html', {
    #     'record': record
    # })


def record_list_pdf(request, queryset):

    response = HttpResponse(content_type='application/pdf')

    obj = queryset.first()
    collection_code = obj.collection_code.name
    queryset = queryset.select_related(
        'county__state_province',
        'country',
        'scientific_name',
        'scientific_name_authorship',
        'order',
        'family',
        'municipality',
        'sampling_protocol',
        'genus'
    )

    # Lo descarga directamente
    # response['Content-Disposition'] = "attachment; filename=certificado.pdf"

    # Lo visualiza
    response['Content-Disposition'] = 'inline; filename=record.pdf'

    html_string = render_to_string('museum/record_list_pdf.html', {
        'records': queryset,
        'collection_code': collection_code
    })

    HTML(
        string=html_string,
        base_url=settings.HOST_URL,
        url_fetcher=django_url_fetcher
    ).write_pdf(response, presentational_hints=True)
    return response
    # return render(request, 'museum/record_list_pdf.html', {
    #     'records': queryset,
    #     'collection_code': collection_code
    # })
