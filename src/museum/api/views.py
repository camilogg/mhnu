from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import CollectionAndNameFilter, RecordFilter
from .serializers import (
    GenusModelSerializer,
    FamilyModelSerializer,
    ScientificNameModelSerializer,
    RecordModelSerializer,
    ContactSerializer
)
from ..models import Genus, ScientificName, Family, Record


class GenusListAPIView(ListAPIView):
    queryset = Genus.objects.all()
    serializer_class = GenusModelSerializer
    pagination_class = None
    filterset_class = CollectionAndNameFilter


class FamilyListAPIView(ListAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilyModelSerializer
    pagination_class = None
    filterset_class = CollectionAndNameFilter


class ScientificNameListAPIView(ListAPIView):
    queryset = ScientificName.objects.all()
    serializer_class = ScientificNameModelSerializer
    pagination_class = None
    filterset_class = CollectionAndNameFilter


class RecordListAPIView(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordModelSerializer
    filterset_class = RecordFilter


class RecordRetrieveAPIView(RetrieveAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordModelSerializer


class ContactAPIView(APIView):
    @swagger_auto_schema(
        request_body=ContactSerializer, responses={status.HTTP_200_OK: ''}
    )
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
