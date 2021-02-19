from django.urls import path

from museum.views import record_detail_pdf

app_name = 'museum'
urlpatterns = [
    path(
        route='record-detail-pdf/<int:pk>/',
        view=record_detail_pdf,
        name='record_detail_pdf'
    )
]
