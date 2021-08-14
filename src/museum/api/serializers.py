from rest_framework import serializers

from ..models import (
    Genus, Family, ScientificName, Record, Country, County, RecordedBy, Type,
    StateProvince
)
from ..tasks import send_mail_contact


class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateProvinceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateProvince
        fields = '__all__'


class CountyModelSerializer(serializers.ModelSerializer):
    state_province = StateProvinceModelSerializer()

    class Meta:
        model = County
        fields = '__all__'


class RecordedByModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordedBy
        fields = '__all__'


class TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class GenusModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = ['id', 'name']


class FamilyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id', 'name']


class ScientificNameModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificName
        fields = ['id', 'name']


class RecordModelSerializer(serializers.ModelSerializer):
    family = FamilyModelSerializer()
    genus = GenusModelSerializer()
    scientific_name = ScientificNameModelSerializer()
    country = CountryModelSerializer()
    county = CountyModelSerializer()
    recorded_by = RecordedByModelSerializer()
    type = TypeModelSerializer()

    class Meta:
        model = Record
        fields = (
            'id', 'family', 'genus', 'scientific_name', 'country', 'county',
            'recorded_by', 'type', 'catalog_number'
        )


class ContactSerializer(serializers.Serializer):
    names = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=50)
    message = serializers.CharField()

    def save(self):
        send_mail_contact.delay(**self.validated_data)
