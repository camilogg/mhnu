from django_filters import CharFilter, FilterSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Member, Slider
from .serializers import MemberModelSerializer, SliderModelSerializer


class NameFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')


class SliderAPIListView(ListAPIView):
    serializer_class = SliderModelSerializer
    queryset = Slider.objects.filter(enabled=True)
    pagination_class = None


class MemberAPIListView(ListAPIView):
    serializer_class = MemberModelSerializer
    queryset = Member.objects.all()
    filterset_class = NameFilter


class MemberRetrieveAPIView(RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberModelSerializer
    lookup_field = 'slug'
