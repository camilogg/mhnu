from django.urls import path

from .api.views import (
    GenusListAPIView,
    FamilyListAPIView,
    ScientificNameListAPIView,
    RecordListAPIView,
    RecordRetrieveAPIView,
    ContactAPIView
)
from museum.views import record_detail_pdf

app_name = 'museum'
urlpatterns = [
    path(
        route='record-detail-pdf/<int:pk>/',
        view=record_detail_pdf,
        name='record_detail_pdf'
    ),

    # Api Urls
    path(
        route='api/genus',
        view=GenusListAPIView.as_view(),
        name='genus'
    ),
    path(
        route='api/families',
        view=FamilyListAPIView.as_view(),
        name='families'
    ),
    path(
        route='api/scientific-names',
        view=ScientificNameListAPIView.as_view(),
        name='scientific_name_list'
    ),
    path(
        route='api/records',
        view=RecordListAPIView.as_view(),
        name='record_list'
    ),
    path(
        route='api/records/<int:pk>',
        view=RecordRetrieveAPIView.as_view(),
        name='record_retrieve'
    ),
    path(
        route='api/contact',
        view=ContactAPIView.as_view(),
        name='contact'
    )
]
