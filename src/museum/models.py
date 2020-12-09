from django.core.validators import RegexValidator, MinValueValidator, \
    MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


# Record Items tables

class Type(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('type')
        verbose_name_plural = _('types')

    def __str__(self):
        return self.name


class CollectionCode(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('collection code')
        verbose_name_plural = _('collection codes')

    def __str__(self):
        return self.name


class BasisOfRecord(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('basis of record')
        verbose_name_plural = _('basis of record')

    def __str__(self):
        return self.name


# Biological Record tables

class RecordedBy(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('recorded by')
        verbose_name_plural = _('recorded by')

    def __str__(self):
        return self.name


class Sex(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('sex')
        verbose_name_plural = _('sexes')

    def __str__(self):
        return self.name


class LifeStage(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('life stage')
        verbose_name_plural = _('life stages')

    def __str__(self):
        return self.name


class OccurrenceStatus(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('occurrence status')
        verbose_name_plural = _('occurrence statuses')

    def __str__(self):
        return self.name


class Preparation(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('preparation')
        verbose_name_plural = _('preparations')

    def __str__(self):
        return self.name


class Disposition(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('disposition')
        verbose_name_plural = _('dispositions')

    def __str__(self):
        return self.name


# Event tables

class SamplingProtocol(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('sampling protocol')
        verbose_name_plural = _('sampling protocols')

    def __str__(self):
        return self.name


class Habitat(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('habitat')
        verbose_name_plural = _('habitats')

    def __str__(self):
        return self.name


# Location tables

class WaterBody(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('water body')
        verbose_name_plural = _('water bodies')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    country_code = models.CharField(
        _('country code'), max_length=2, unique=True
    )

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')

    def __str__(self):
        return self.name


class StateProvince(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_('country')
    )

    class Meta:
        verbose_name = _('state province')
        verbose_name_plural = _('state provinces')

    def __str__(self):
        return self.name


class County(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    state_province = models.ForeignKey(
        StateProvince, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_('state province')
    )

    class Meta:
        verbose_name = _('county')
        verbose_name_plural = _('counties')

    def __str__(self):
        return self.name


class Municipality(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_('county')
    )

    class Meta:
        verbose_name = _('municipality')
        verbose_name_plural = _('municipalities')

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    verbatim_locality = models.CharField(
        _('verbatim locality'), max_length=255, blank=True
    )
    municipality = models.ForeignKey(
        Municipality, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_('county')
    )

    class Meta:
        verbose_name = _('locality')
        verbose_name_plural = _('localities')

    def __str__(self):
        return self.name


class Record(models.Model):
    class Continents(models.TextChoices):
        AFRICA = 'AF', _('Africa')
        ASIA = 'AS', _('Asia')
        EUROPE = 'EU', _('Europe')
        NORTH_AMERICA = 'NA', _('North America')
        SOUTH_AMERICA = 'SA', _('South America')
        OCEANIA = 'OC', _('Oceania')
        ANTARCTICA = 'AN', _('Antarctica')

    class VerbatimCoordinatesSystem(models.TextChoices):
        DECIMAL_DEGREES = 'Grados decimales', _('Decimal degrees')
        DEGREES_DECIMAL_MINUTES = 'Grados, minutos decimales', _(
            'Degrees, decimal minutes'
        )
        DEGREES_MINUTES_SECONDS = 'Grados, minutos, segundos', _(
            'Degrees, minutes, seconds'
        )
        UTM = 'UTM', _('UTM')
        CRTM = 'CRTM', _('CRTM')

    class GeoreferenceVerificationStatus(models.TextChoices):
        NO_VERIFICATION = 'Sin verificación', _('No verification')
        VERIFIED = 'Verificado por el custodio de los datos', _(
            'Verified by the custodian of the data'
        )
        VERIFIED_BY_DATA_PROVIDER = \
            'Verificado por el proveedor de los datos', _(
                'Verified by the data provider'
            )

    # Record Items Fields
    type = models.ForeignKey(
        Type, on_delete=models.CASCADE, verbose_name=_('type')
    )
    modified = models.DateField(_('modified'), blank=True, null=True)
    language = models.CharField(_('language'), max_length=2, default='es')
    license = models.CharField(_('license'), max_length=255, blank=True)
    rights_holder = models.CharField(
        _('rights holder'), max_length=255,
        default='Universidad de los Llanos (Unillanos)'
    )
    access_rights = models.CharField(
        _('access rights'), max_length=255, default='Sólo uso científico'
    )
    bibliographic_citation = models.TextField(
        _('bibliographic citation'), blank=True
    )
    references = models.TextField(_('references'), blank=True)
    institution_ID = models.CharField(
        _('institution ID'), default='892000757-3', max_length=255
    )
    collection_ID = models.CharField(
        _('collection ID'), blank=True, max_length=255
    )
    dataset_ID = models.CharField(_('dataset ID'), max_length=255, blank=True)
    institution_code = models.CharField(
        _('institution code'), max_length=255, default='Unillanos'
    )
    collection_code = models.ForeignKey(
        CollectionCode, on_delete=models.CASCADE,
        verbose_name=_('collection code')
    )
    dataset_name = models.CharField(
        _('dataset name'), max_length=255, blank=True
    )
    owner_institution_code = models.CharField(
        _('owner institution code'), max_length=255, blank=True
    )
    basis_of_record = models.ForeignKey(
        BasisOfRecord, on_delete=models.CASCADE,
        verbose_name=_('basis of record')
    )
    information_withheld = models.TextField(
        _('information withheld'), blank=True
    )
    data_generalizations = models.TextField(
        _('data generalizations'), blank=True
    )
    dynamic_properties = models.JSONField(
        _('dynamic properties'), blank=True, null=True
    )

    # Biological Record fields
    occurrence_id_regex = RegexValidator(
        regex=r'Unillanos:MHNU-[A-Z]{1,2}:\d+',
        message=_('Invalid format')
    )
    occurrence_ID = models.CharField(
        _('occurrence ID'), max_length=255, validators=[occurrence_id_regex],
        unique=True
    )
    catalog_number = models.CharField(
        _('catalog number'), max_length=255, unique=True
    )
    occurrence_remarks = models.TextField(
        _('occurrence remarks'), blank=True
    )
    record_number = models.CharField(
        _('record number'), max_length=255, unique=True, null=True, blank=True
    )
    recorded_by = models.ForeignKey(
        RecordedBy, on_delete=models.CASCADE, verbose_name=_('recorded by')
    )
    organism_ID = models.CharField(
        _('organism ID'), max_length=255, blank=True
    )
    individual_count = models.PositiveSmallIntegerField(_('individual count'))
    sex = models.ForeignKey(
        Sex, on_delete=models.CASCADE, verbose_name=_('sex')
    )
    life_stage = models.ForeignKey(
        LifeStage, on_delete=models.CASCADE, verbose_name=_('life stage')
    )
    reproductive_condition = models.CharField(
        _('reproductive condition'), max_length=255, blank=True
    )
    behavior = models.CharField(_('behavior'), max_length=255, blank=True)
    establishment_means = models.CharField(
        _('establishment means'), max_length=255, blank=True
    )
    occurrence_status = models.ForeignKey(
        OccurrenceStatus, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name=_('occurrence status')
    )
    preparations = models.ForeignKey(
        Preparation, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name=_('preparations')
    )
    disposition = models.ForeignKey(
        Disposition, on_delete=models.CASCADE, null=True, blank=True,
        verbose_name=_('disposition')
    )
    other_catalog_numbers = models.CharField(
        _('other catalog numbers'), max_length=255, blank=True
    )
    previous_identifications = models.CharField(
        _('previous identifications'), max_length=255, blank=True
    )
    associated_media = models.CharField(
        _('associated media'), max_length=255, blank=True
    )
    associated_references = models.CharField(
        _('associated references'), max_length=255, blank=True
    )
    associated_occurrences = models.CharField(
        _('associated occurrences'), max_length=255, blank=True
    )
    associated_sequences = models.CharField(
        _('associated sequences'), max_length=255, blank=True
    )
    associated_taxa = models.CharField(
        _('associated taxa'), max_length=255, blank=True
    )

    # Event fields
    event_ID = models.CharField(_('event ID'), max_length=255, blank=True)
    parent_event_ID = models.CharField(
        _('parent event ID'), max_length=255, blank=True
    )
    sampling_protocol = models.ForeignKey(
        SamplingProtocol, on_delete=models.CASCADE,
        verbose_name=_('sampling protocol'), blank=True, null=True
    )
    sampling_effort = models.CharField(
        _('sampling effort'), max_length=255, blank=True
    )
    sampling_size_value = models.PositiveSmallIntegerField(
        _('sampling size value'), blank=True, null=True
    )
    sampling_size_unit = models.CharField(
        _('sampling size unit'), max_length=255, blank=True
    )
    event_date = models.DateField(_('event date'), blank=True, null=True)
    event_time = models.TimeField(_('event time'), blank=True, null=True)
    start_day_of_year = models.PositiveSmallIntegerField(
        _('start day of year'), blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(366)]
    )
    end_day_of_year = models.PositiveSmallIntegerField(
        _('end day of year'), blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(366)]
    )
    year = models.PositiveSmallIntegerField(_('year'), blank=True, null=True)
    month = models.PositiveSmallIntegerField(
        _('month'), blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    day = models.PositiveSmallIntegerField(
        _('day'), blank=True, null=True,
        validators=[MinValueValidator(1), MaxValueValidator(31)]
    )
    verbatim_event_date = models.CharField(
        _('verbatim event date'), max_length=255, blank=True
    )
    habitat = models.ForeignKey(
        Habitat, on_delete=models.CASCADE, verbose_name=_('habitat'),
        blank=True, null=True
    )
    field_number = models.CharField(
        _('field number'), max_length=255, blank=True
    )
    field_notes = models.TextField(_('field notes'), blank=True)
    event_remarks = models.TextField(_('event remarks'), blank=True)

    # Location fields
    location_ID = models.CharField(
        _('location ID'), max_length=255, blank=True
    )
    higher_geography_ID = models.CharField(
        _(' higher geography ID'), max_length=255, blank=True
    )
    higher_geography = models.CharField(
        _(' higher geography'), max_length=255, blank=True
    )
    continent = models.CharField(
        _('continent'), max_length=2, choices=Continents.choices,
        default=Continents.SOUTH_AMERICA
    )
    water_body = models.ForeignKey(
        WaterBody, on_delete=models.CASCADE, verbose_name=_('water body'),
        blank=True, null=True
    )
    island_group = models.CharField(
        _('island group'), max_length=255, blank=True
    )
    island = models.CharField(_('island'), max_length=255, blank=True)
    locality = models.ForeignKey(
        Locality, on_delete=models.CASCADE, verbose_name=_('locality'),
        blank=True, null=True
    )
    verbatim_elevation = models.CharField(
        _('verbatim elevation'), blank=True, max_length=255
    )
    minimum_elevation_in_meters = models.PositiveSmallIntegerField(
        _('minimum elevation in meters'), blank=True, null=True
    )
    maximum_elevation_in_meters = models.PositiveSmallIntegerField(
        _('maximum elevation in meters'), blank=True, null=True
    )
    verbatim_depth = models.CharField(
        _('verbatim depth'), max_length=255, blank=True
    )
    minimum_depth_in_meters = models.PositiveSmallIntegerField(
        _('minimum depth in meters'), blank=True, null=True
    )
    maximum_depth_in_meters = models.PositiveSmallIntegerField(
        _('maximum depth in meters'), blank=True, null=True
    )
    minimum_distance_above_surface_in_meters = models.CharField(
        _('minimum distance above surface in meters'), max_length=255,
        blank=True
    )
    maximum_distance_above_surface_in_meters = models.CharField(
        _('maximum distance above surface in meters'), max_length=255,
        blank=True
    )
    location_according_to = models.CharField(
        _('location according to'), max_length=255, blank=True
    )
    location_remarks = models.TextField(_('location remarks'), blank=True)
    verbatim_coordinates = models.CharField(
        _('verbatim coordinates'), max_length=255, blank=True
    )
    verbatim_latitude = models.CharField(
        _('verbatim latitude'), max_length=255, blank=True
    )
    verbatim_longitude = models.CharField(
        _('verbatim longitude'), max_length=255, blank=True
    )
    verbatim_coordinate_system = models.CharField(
        _('verbatim coordinate system'), max_length=50, blank=True,
        choices=VerbatimCoordinatesSystem.choices,
        default=VerbatimCoordinatesSystem.DEGREES_MINUTES_SECONDS
    )
    verbatim_SRS = models.CharField(
        _('verbatim SRS'), max_length=255, blank=True
    )
    decimal_latitude = models.FloatField(
        _('decimal latitude'), blank=True, null=True
    )
    decimal_longitude = models.FloatField(
        _('decimal longitude'), blank=True, null=True
    )
    geodetic_datum = models.CharField(
        _('geodetic datum'), max_length=255, default='WGS84'
    )
    coordinate_uncertainty_in_meters = models.PositiveSmallIntegerField(
        _('coordinate uncertainty in meters'), blank=True, null=True
    )
    coordinate_precision = models.FloatField(
        _('coordinate precision'), blank=True, null=True
    )
    point_radius_spatial_fit = models.CharField(
        _('point radius spatial fit'), max_length=255, blank=True
    )
    footprint_WKT = models.CharField(
        _('footprint WKT'), max_length=255, blank=True
    )
    footprint_SRS = models.CharField(
        _('footprint SRS'), max_length=255, blank=True
    )
    footprint_spatial_fit = models.CharField(
        _('footprint spatial fit'), max_length=255, blank=True
    )
    georeferenced_by = models.TextField(_('georeferenced by'), blank=True)
    georeferenced_date = models.CharField(
        _('georeferenced date'), max_length=255, blank=True
    )
    georeference_protocol = models.CharField(
        _('georeference protocol'), max_length=255, blank=True
    )
    georeference_sources = models.CharField(
        _('georeference sources'), max_length=255, blank=True
    )
    georeference_verification_status = models.CharField(
        _('georeference verification status'), max_length=255, blank=True,
        choices=GeoreferenceVerificationStatus.choices
    )
    georeference_remarks = models.TextField(
        _('georeference remarks'), blank=True
    )

    class Meta:
        verbose_name = _('record')
        verbose_name_plural = _('records')

    def __str__(self):
        return self.occurrence_ID
