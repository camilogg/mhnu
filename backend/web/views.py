from rest_framework.generics import ListAPIView

from .models import Slider, Member
from .serializers import SliderModelSerializer, MemberModelSerializer


class SliderAPIListView(ListAPIView):
    serializer_class = SliderModelSerializer
    queryset = Slider.objects.filter(enabled=True)
    pagination_class = None


class MemberAPIListView(ListAPIView):
    serializer_class = MemberModelSerializer
    queryset = Member.objects.all()
    pagination_class = None
