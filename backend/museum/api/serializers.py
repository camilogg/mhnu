from rest_framework import serializers
from drf_recaptcha.fields import ReCaptchaV2Field

from ..models import (
    Genus, Family, ScientificName, Record, Country, County, RecordedBy, Type,
    StateProvince, IdentifiedBy, Kingdom, Phylum, Class, Order,
    SpecificEpithet, TaxonRank, ScientificNameAuthorship, NomenclaturalCode,
    Locality, Image
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


class IdentifiedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentifiedBy
        fields = ['id', 'name']


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        fields = ['id', 'name']


class PhylumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phylum
        fields = ['id', 'name']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'name']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name']


class SpecificEpithetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificEpithet
        fields = ['id', 'name']


class TaxonRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxonRank
        fields = ['id', 'name']


class ScientificNameAuthorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificNameAuthorship
        fields = ['id', 'name']


class NomenclaturalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NomenclaturalCode
        fields = ['id', 'name']


class LocalityCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = ['id', 'name']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class RecordModelSerializer(serializers.ModelSerializer):
    family = FamilyModelSerializer()
    genus = GenusModelSerializer()
    scientific_name = ScientificNameModelSerializer()
    country = CountryModelSerializer()
    county = CountyModelSerializer()
    recorded_by = RecordedByModelSerializer()
    type = TypeModelSerializer()
    identified_by = IdentifiedBySerializer()
    kingdom = KingdomSerializer()
    phylum = PhylumSerializer()
    _class = ClassSerializer()
    order = OrderSerializer()
    specific_epithet = SpecificEpithetSerializer()
    taxon_rank = TaxonRankSerializer()
    scientific_name_authorship = ScientificNameAuthorshipSerializer()
    nomenclatural_code = NomenclaturalCodeSerializer()
    images = ImageSerializer(many=True)

    class Meta:
        model = Record
        fields = (
            'id', 'family', 'genus', 'scientific_name', 'country', 'county',
            'recorded_by', 'type', 'catalog_number', 'record_number',
            'georeferenced_by', 'identified_by', 'kingdom', 'phylum', '_class',
            'order', 'specific_epithet', 'taxon_rank', 'nomenclatural_code',
            'scientific_name_authorship', 'locality', 'geodetic_datum',
            'minimum_elevation_in_meters', 'maximum_elevation_in_meters',
            'verbatim_latitude', 'verbatim_longitude', 'decimal_latitude',
            'decimal_longitude', 'images', 'slug'
        )


class ContactSerializer(serializers.Serializer):
    names = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=50)
    message = serializers.CharField()
    token = ReCaptchaV2Field()

    def save(self):
        send_mail_contact.delay(**self.validated_data)

    def validate(self, attrs):
        attrs.pop('token')
        return attrs
