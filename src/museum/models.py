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


class Record(models.Model):
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

    class Meta:
        verbose_name = _('record')
        verbose_name_plural = _('records')

    def __str__(self):
        return self.occurrence_ID
