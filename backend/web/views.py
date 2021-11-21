from django_filters import FilterSet, CharFilter
from rest_framework.generics import ListAPIView

from .models import Slider, Member, Post
from .serializers import (
    SliderModelSerializer,
    MemberModelSerializer,
    PostModelSerializer
)


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


class PostAPIListView(ListAPIView):
    serializer_class = PostModelSerializer
    queryset = Post.objects.all()
    filterset_class = NameFilter
