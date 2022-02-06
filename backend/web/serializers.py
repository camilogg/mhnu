from rest_framework.serializers import ModelSerializer

from .models import Member, Slider


class SliderModelSerializer(ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'name', 'image')


class MemberModelSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'image', 'position', 'description', 'slug')
