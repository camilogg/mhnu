from rest_framework import serializers

from .models import Slider, Member


class SliderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'name', 'image')


class MemberModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'image', 'position')
