from rest_framework.serializers import ModelSerializer

from .models import Slider, Member, PostImage, Post


class SliderModelSerializer(ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'name', 'image')


class MemberModelSerializer(ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name', 'image', 'position', 'description')


class PostImageModelSerializer(ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('id', 'name', 'image')


class PostModelSerializer(ModelSerializer):
    images = PostImageModelSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'name', 'cover', 'content', 'images')
