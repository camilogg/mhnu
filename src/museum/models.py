from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Record Items tables
from MHNU.settings.base import resource
from museum.validators import occurrence_id_regex, date_regex, \
    validate_date_range


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

    # country = models.ForeignKey(
    #     Country, on_delete=models.CASCADE, blank=True, null=True,
    #     verbose_name=_('country')
    # )

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

    # county = models.ForeignKey(
    #     County, on_delete=models.CASCADE, blank=True, null=True,
    #     verbose_name=_('county')
    # )

    class Meta:
        verbose_name = _('municipality')
        verbose_name_plural = _('municipalities')

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)
    verbatim_locality = models.CharField(
        _('verbatim locality'), max_length=255, blank=True, null=True
    )

    # municipality = models.ForeignKey(
    #     Municipality, on_delete=models.CASCADE, blank=True, null=True,
    #     verbose_name=_('county')
    # )

    class Meta:
        verbose_name = _('locality')
        verbose_name_plural = _('localities')

    def __str__(self):
        return self.name


# Identification tables

class IdentifiedBy(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('Identified by')
        verbose_name_plural = _('Identified by')

    def __str__(self):
        return self.name


# Taxon tables

class ScientificName(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('scientific name')
        verbose_name_plural = _('scientific names')

    def __str__(self):
        return self.name


class Kingdom(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('kingdom')
        verbose_name_plural = _('kingdoms')

    def __str__(self):
        return self.name


class Phylum(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('phylum')
        verbose_name_plural = _('phylum')

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('class')
        verbose_name_plural = _('classes')

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')

    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('family')
        verbose_name_plural = _('families')

    def __str__(self):
        return self.name


class Genus(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('genus')
        verbose_name_plural = _('genuses')

    def __str__(self):
        return self.name


class SpecificEpithet(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('specific epithet')
        verbose_name_plural = _('specific epithets')

    def __str__(self):
        return self.name


class TaxonRank(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('taxon rank')
        verbose_name_plural = _('taxon ranks')

    def __str__(self):
        return self.name


class ScientificNameAuthorship(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('scientific name authorship')
        verbose_name_plural = _('scientific name authorships')

    def __str__(self):
        return self.name


class VernacularName(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('vernacular name')
        verbose_name_plural = _('vernacular names')

    def __str__(self):
        return self.name


class NomenclaturalCode(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('nomenclatural code')
        verbose_name_plural = _('nomenclatural codes')

    def __str__(self):
        return self.name


class TaxonomicStatus(models.Model):
    name = models.CharField(_('name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _('taxonomic status')
        verbose_name_plural = _('taxonomic statuses')

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
        DECIMAL_DEGREES = 'grados decimales', _('Decimal degrees')
        DEGREES_DECIMAL_MINUTES = 'grados minutos decimales', _(
            'Degrees, decimal minutes'
        )
        DEGREES_MINUTES_SECONDS = 'grados minutos segundos', _(
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
    license = models.CharField(
        _('license'), max_length=255, blank=True, null=True
    )
    rights_holder = models.CharField(
        _('rights holder'), max_length=255,
        default='Universidad de los Llanos (Unillanos)'
    )
    access_rights = models.CharField(
        _('access rights'), max_length=255, default='Sólo uso científico'
    )
    bibliographic_citation = models.TextField(
        _('bibliographic citation'), blank=True, null=True
    )
    references = models.TextField(_('references'), blank=True, null=True)
    institution_ID = models.CharField(
        _('institution ID'), default='892000757-3', max_length=255
    )
    collection_ID = models.CharField(
        _('collection ID'), blank=True, max_length=255, null=True
    )
    dataset_ID = models.CharField(
        _('dataset ID'), max_length=255, blank=True, null=True
    )
    institution_code = models.CharField(
        _('institution code'), max_length=255, default='Unillanos'
    )
    collection_code = models.ForeignKey(
        CollectionCode, on_delete=models.CASCADE,
        verbose_name=_('collection code')
    )
    dataset_name = models.CharField(
        _('dataset name'), max_length=255, blank=True, null=True
    )
    owner_institution_code = models.CharField(
        _('owner institution code'), max_length=255, blank=True, null=True
    )
    basis_of_record = models.ForeignKey(
        BasisOfRecord, on_delete=models.CASCADE,
        verbose_name=_('basis of record')
    )
    information_withheld = models.TextField(
        _('information withheld'), blank=True, null=True
    )
    data_generalizations = models.TextField(
        _('data generalizations'), blank=True, null=True
    )
    dynamic_properties = models.JSONField(
        _('dynamic properties'), blank=True, null=True
    )

    # Biological Record fields
    occurrence_ID = models.CharField(
        _('occurrence ID'), max_length=255, validators=[occurrence_id_regex],
        unique=True
    )
    catalog_number = models.CharField(
        _('catalog number'), max_length=255, unique=True
    )
    occurrence_remarks = models.TextField(
        _('occurrence remarks'), blank=True, null=True
    )
    record_number = models.CharField(
        _('record number'), max_length=255, unique=True, null=True, blank=True
    )
    recorded_by = models.ForeignKey(
        RecordedBy, on_delete=models.CASCADE, verbose_name=_('recorded by'),
        blank=True, null=True
    )
    organism_ID = models.CharField(
        _('organism ID'), max_length=255, blank=True, null=True
    )
    organism_quantity = models.CharField(
        _('organism quantity'), max_length=255, blank=True, null=True
    )
    organism_quantity_type = models.CharField(
        _('organism quantity type'), max_length=255, blank=True, null=True
    )
    organism_name = models.CharField(
        _('organism name'), max_length=255, blank=True, null=True
    )
    organism_scope = models.CharField(
        _('organism scope'), max_length=255, blank=True, null=True
    )
    associated_organisms = models.TextField(
        _('associated organisms'), blank=True, null=True
    )
    organism_remarks = models.TextField(
        _('organism remarks'), blank=True, null=True
    )
    individual_count = models.PositiveSmallIntegerField(_('individual count'))
    sex = models.ForeignKey(
        Sex, on_delete=models.CASCADE, verbose_name=_('sex'),
        blank=True, null=True
    )
    life_stage = models.ForeignKey(
        LifeStage, on_delete=models.CASCADE, verbose_name=_('life stage'),
        blank=True, null=True
    )
    reproductive_condition = models.CharField(
        _('reproductive condition'), max_length=255, blank=True, null=True
    )
    behavior = models.CharField(
        _('behavior'), max_length=255, blank=True, null=True
    )
    establishment_means = models.CharField(
        _('establishment means'), max_length=255, blank=True, null=True
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
        _('other catalog numbers'), max_length=255, blank=True, null=True
    )
    previous_identifications = models.CharField(
        _('previous identifications'), max_length=255, blank=True, null=True
    )
    associated_media = models.CharField(
        _('associated media'), max_length=255, blank=True, null=True
    )
    associated_references = models.CharField(
        _('associated references'), max_length=255, blank=True, null=True
    )
    associated_occurrences = models.CharField(
        _('associated occurrences'), max_length=255, blank=True, null=True
    )
    associated_sequences = models.CharField(
        _('associated sequences'), max_length=255, blank=True, null=True
    )
    associated_taxa = models.CharField(
        _('associated taxa'), max_length=255, blank=True, null=True
    )
    material_sample_ID = models.CharField(
        _('material_sample_ID'), max_length=255, blank=True, null=True
    )

    # Event fields
    event_ID = models.CharField(
        _('event ID'), max_length=255, blank=True, null=True
    )
    parent_event_ID = models.CharField(
        _('parent event ID'), max_length=255, blank=True, null=True
    )
    sampling_protocol = models.ForeignKey(
        SamplingProtocol, on_delete=models.CASCADE,
        verbose_name=_('sampling protocol'), blank=True, null=True
    )
    sampling_effort = models.CharField(
        _('sampling effort'), max_length=255, blank=True, null=True
    )
    sampling_size_value = models.PositiveSmallIntegerField(
        _('sampling size value'), blank=True, null=True
    )
    sampling_size_unit = models.CharField(
        _('sampling size unit'), max_length=255, blank=True, null=True
    )
    event_date = models.CharField(
        _('event date'), max_length=255, blank=True, null=True,
        validators=[date_regex, validate_date_range]
    )
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
        _('verbatim event date'), max_length=255, blank=True, null=True,
        validators=[date_regex, validate_date_range]
    )
    habitat = models.ForeignKey(
        Habitat, on_delete=models.CASCADE, verbose_name=_('habitat'),
        blank=True, null=True
    )
    field_number = models.CharField(
        _('field number'), max_length=255, blank=True, null=True
    )
    field_notes = models.TextField(_('field notes'), blank=True, null=True)
    event_remarks = models.TextField(_('event remarks'), blank=True, null=True)

    # Location fields
    location_ID = models.CharField(
        _('location ID'), max_length=255, blank=True, null=True
    )
    higher_geography_ID = models.CharField(
        _(' higher geography ID'), max_length=255, blank=True, null=True
    )
    higher_geography = models.CharField(
        _(' higher geography'), max_length=255, blank=True, null=True
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
        _('island group'), max_length=255, blank=True, null=True
    )
    island = models.CharField(
        _('island'), max_length=255, blank=True, null=True
    )
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, verbose_name=_('country')
    )
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, verbose_name=_('county'),
        blank=True, null=True
    )
    municipality = models.ForeignKey(
        Municipality, on_delete=models.CASCADE, verbose_name=_('municipality'),
        blank=True, null=True
    )
    locality = models.ForeignKey(
        Locality, on_delete=models.CASCADE, verbose_name=_('locality'),
        blank=True, null=True
    )
    verbatim_elevation = models.CharField(
        _('verbatim elevation'), blank=True, max_length=255, null=True
    )
    minimum_elevation_in_meters = models.PositiveSmallIntegerField(
        _('minimum elevation in meters'), blank=True, null=True
    )
    maximum_elevation_in_meters = models.PositiveSmallIntegerField(
        _('maximum elevation in meters'), blank=True, null=True
    )
    verbatim_depth = models.CharField(
        _('verbatim depth'), max_length=255, blank=True, null=True
    )
    minimum_depth_in_meters = models.PositiveSmallIntegerField(
        _('minimum depth in meters'), blank=True, null=True
    )
    maximum_depth_in_meters = models.PositiveSmallIntegerField(
        _('maximum depth in meters'), blank=True, null=True
    )
    minimum_distance_above_surface_in_meters = models.CharField(
        _('minimum distance above surface in meters'), max_length=255,
        blank=True, null=True
    )
    maximum_distance_above_surface_in_meters = models.CharField(
        _('maximum distance above surface in meters'), max_length=255,
        blank=True, null=True
    )
    location_according_to = models.CharField(
        _('location according to'), max_length=255, blank=True, null=True
    )
    location_remarks = models.TextField(
        _('location remarks'), blank=True, null=True
    )
    verbatim_coordinates = models.CharField(
        _('verbatim coordinates'), max_length=255, blank=True, null=True
    )
    verbatim_latitude = models.CharField(
        _('verbatim latitude'), max_length=255, blank=True, null=True
    )
    verbatim_longitude = models.CharField(
        _('verbatim longitude'), max_length=255, blank=True, null=True
    )
    verbatim_coordinate_system = models.CharField(
        _('verbatim coordinate system'), max_length=50, blank=True,
        choices=VerbatimCoordinatesSystem.choices,
        default=VerbatimCoordinatesSystem.DEGREES_MINUTES_SECONDS
    )
    verbatim_SRS = models.CharField(
        _('verbatim SRS'), max_length=255, blank=True, null=True
    )
    decimal_latitude = models.FloatField(
        _('decimal latitude'), blank=True, null=True
    )
    decimal_longitude = models.FloatField(
        _('decimal longitude'), blank=True, null=True
    )
    geodetic_datum = models.CharField(
        _('geodetic datum'), max_length=255, default='WGS84', null=True
    )
    coordinate_uncertainty_in_meters = models.PositiveSmallIntegerField(
        _('coordinate uncertainty in meters'), blank=True, null=True
    )
    coordinate_precision = models.FloatField(
        _('coordinate precision'), blank=True, null=True
    )
    point_radius_spatial_fit = models.CharField(
        _('point radius spatial fit'), max_length=255, blank=True, null=True
    )
    footprint_WKT = models.CharField(
        _('footprint WKT'), max_length=255, blank=True, null=True
    )
    footprint_SRS = models.CharField(
        _('footprint SRS'), max_length=255, blank=True, null=True
    )
    footprint_spatial_fit = models.CharField(
        _('footprint spatial fit'), max_length=255, blank=True, null=True
    )
    georeferenced_by = models.TextField(
        _('georeferenced by'), blank=True, null=True
    )
    georeferenced_date = models.CharField(
        _('georeferenced date'), max_length=255, blank=True, null=True,
        validators=[date_regex, validate_date_range]
    )
    georeference_protocol = models.CharField(
        _('georeference protocol'), max_length=255, blank=True, null=True
    )
    georeference_sources = models.CharField(
        _('georeference sources'), max_length=255, blank=True, null=True
    )
    georeference_verification_status = models.CharField(
        _('georeference verification status'), max_length=255, blank=True,
        choices=GeoreferenceVerificationStatus.choices, null=True
    )
    georeference_remarks = models.TextField(
        _('georeference remarks'), blank=True, null=True
    )

    # Biological context fields
    geological_context_ID = models.CharField(
        _('geological context ID'), max_length=255, blank=True, null=True
    )
    earliest_eon_or_lowest_eonothem = models.CharField(
        _('earliest eon or lowest eonothem'), max_length=255, blank=True,
        null=True
    )
    latest_eon_or_highest_eonothem = models.CharField(
        _('latest eon or highest eonothem'), max_length=255, blank=True,
        null=True
    )
    earliest_era_or_lowest_erathem = models.CharField(
        _('earliest era or lowest erathem'), max_length=255, blank=True,
        null=True
    )
    latest_era_or_highest_erathem = models.CharField(
        _('latest era or highest erathem'), max_length=255, blank=True,
        null=True
    )
    earliest_period_or_lowest_system = models.CharField(
        _('earliest period or lowest system'), max_length=255, blank=True,
        null=True
    )
    latest_period_or_highest_system = models.CharField(
        _('latest period or highest system'), max_length=255, blank=True,
        null=True
    )
    earliest_epoch_or_lowest_series = models.CharField(
        _('earliest epoch or lowest series'), max_length=255, blank=True,
        null=True
    )
    latest_epoch_or_highest_series = models.CharField(
        _('latest epoch or highest series'), max_length=255, blank=True,
        null=True
    )
    earliest_age_or_lowest_stage = models.CharField(
        _('earliest age or lowest stage'), max_length=255, blank=True,
        null=True
    )
    latest_age_or_highest_stage = models.CharField(
        _('latest age or highest stage'), max_length=255, blank=True,
        null=True
    )
    lowest_biostratigraphic_zone = models.CharField(
        _('lowest biostratigraphic zone'), max_length=255, blank=True,
        null=True
    )
    highest_biostratigraphic_zone = models.CharField(
        _('highest biostratigraphic zone'), max_length=255, blank=True,
        null=True
    )
    lithostratigraphic_terms = models.CharField(
        _('lithostratigraphic terms'), max_length=255, blank=True,
        null=True
    )
    group = models.CharField(_('group'), max_length=255, blank=True, null=True)
    formation = models.CharField(
        _('formation'), max_length=255, blank=True, null=True
    )
    member = models.CharField(
        _('member'), max_length=255, blank=True, null=True
    )
    bed = models.CharField(_('bed'), max_length=255, blank=True, null=True)

    # Identification fields
    identification_ID = models.CharField(
        _('identification ID'), max_length=255, blank=True, null=True
    )
    identified_by = models.ForeignKey(
        IdentifiedBy, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_('identified by')
    )
    date_identified = models.DateField(
        _('date identified'), blank=True, null=True,
        validators=[date_regex, validate_date_range]
    )
    identification_references = models.TextField(
        _('identification references'), blank=True, null=True
    )
    identification_verification_status = models.CharField(
        _('identification verification status'), blank=True, max_length=255,
        null=True
    )
    identification_remarks = models.TextField(
        _('identification remarks'), blank=True, null=True
    )
    identification_qualifier = models.TextField(
        _('identification qualifier'), blank=True, null=True
    )
    type_status = models.TextField(_('type status'), blank=True, null=True)

    # Taxon fields
    taxon_ID = models.CharField(
        _('taxon ID'), max_length=255, blank=True, null=True
    )
    scientific_name_ID = models.CharField(
        _('scientific name ID'), max_length=255, blank=True, null=True
    )
    accepted_name_usage_ID = models.CharField(
        _('accepted name usage ID'), max_length=255, blank=True, null=True
    )
    parent_name_usage_ID = models.CharField(
        _('parent name usage ID'), max_length=255, blank=True, null=True
    )
    original_name_usage_ID = models.CharField(
        _('original name usage ID'), max_length=255, blank=True, null=True
    )
    name_according_to_ID = models.CharField(
        _('name according to ID'), max_length=255, blank=True, null=True
    )
    name_published_in_ID = models.CharField(
        _('name published in ID'), max_length=255, blank=True, null=True
    )
    taxon_concept_ID = models.CharField(
        _('taxon concept ID'), max_length=255, blank=True, null=True
    )
    scientific_name = models.ForeignKey(
        ScientificName, verbose_name=_('scientific name'),
        on_delete=models.CASCADE, blank=True, null=True
    )
    accepted_name_usage = models.CharField(
        _('accepted name usage'), max_length=255, blank=True, null=True
    )
    parent_name_usage = models.CharField(
        _('parent name usage'), max_length=255, blank=True, null=True
    )
    original_name_usage = models.CharField(
        _('original name usage'), max_length=255, blank=True, null=True
    )
    name_according_to = models.TextField(
        _('name according to'), blank=True, null=True
    )
    name_published_in = models.TextField(
        _('name published in'), blank=True, null=True
    )
    name_published_in_year = models.PositiveSmallIntegerField(
        _('name published in year'), blank=True, null=True
    )
    higher_classification = models.TextField(
        _('higher classification'), blank=True, null=True
    )
    kingdom = models.ForeignKey(
        Kingdom, on_delete=models.CASCADE, verbose_name=_('kingdom'),
        blank=True, null=True
    )
    phylum = models.ForeignKey(
        Phylum, on_delete=models.CASCADE, verbose_name=_('phylum'),
        blank=True, null=True
    )
    _class = models.ForeignKey(
        Class, on_delete=models.CASCADE, verbose_name=_('class'),
        blank=True, null=True
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, verbose_name=_('order'),
        blank=True, null=True
    )
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, verbose_name=_('family'),
        blank=True, null=True
    )
    genus = models.ForeignKey(
        Genus, on_delete=models.CASCADE, verbose_name=_('genus'),
        blank=True, null=True
    )
    subgenus = models.CharField(
        _('subgenus'), max_length=255, blank=True, null=True
    )
    specific_epithet = models.ForeignKey(
        SpecificEpithet, on_delete=models.CASCADE,
        verbose_name=_('specific epithet'), blank=True, null=True
    )
    infraspecific_epithet = models.CharField(
        _('infraspecific epithet'), max_length=255, blank=True, null=True
    )
    taxon_rank = models.ForeignKey(
        TaxonRank, on_delete=models.CASCADE, verbose_name=_('taxon rank'),
        blank=True, null=True
    )
    verbatim_taxon_rank = models.CharField(
        _('verbatim taxon rank'), max_length=255, blank=True, null=True
    )
    scientific_name_authorship = models.ForeignKey(
        ScientificNameAuthorship, on_delete=models.CASCADE,
        verbose_name=_('scientific name authorship'), blank=True, null=True
    )
    vernacular_name = models.ForeignKey(
        VernacularName, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_('vernacular name')
    )
    nomenclatural_code = models.ForeignKey(
        NomenclaturalCode, on_delete=models.CASCADE,
        verbose_name=_('nomenclatural code'), blank=True, null=True
    )
    taxonomic_status = models.ForeignKey(
        TaxonomicStatus, on_delete=models.CASCADE, blank=True, null=True,
        verbose_name=_('taxonomic status')
    )
    nomenclatural_status = models.CharField(
        _('nomenclatural status'), max_length=255, blank=True, null=True
    )
    taxon_remarks = models.TextField(_('taxon remarks'), blank=True, null=True)

    class Meta:
        verbose_name = _('record')
        verbose_name_plural = _('records')

    def __str__(self):
        return self.occurrence_ID

    @classmethod
    def export_resource_classes(cls):
        return {
            'records': (
                'Records resource', resource()
            )
        }
