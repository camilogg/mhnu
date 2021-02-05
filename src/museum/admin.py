from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django_object_actions import DjangoObjectActions

from import_export.admin import ImportExportModelAdmin

from import_export_celery.models import ExportJob
from .models import (
    Record,
    Type,
    CollectionCode,
    BasisOfRecord,
    Sex,
    LifeStage,
    OccurrenceStatus,
    Preparation,
    Disposition,
    RecordedBy,
    SamplingProtocol,
    Habitat,
    WaterBody,
    Country,
    StateProvince,
    County,
    Municipality,
    Locality,
    IdentifiedBy,
    ScientificName,
    Kingdom,
    Phylum,
    Class,
    Order,
    Family,
    Genus,
    SpecificEpithet,
    TaxonRank,
    ScientificNameAuthorship,
    VernacularName,
    NomenclaturalCode,
    TaxonomicStatus
)
from .resources import RecordModelResource


@admin.register(RecordedBy)
class RecordedByAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    formfield_overrides = {
        models.CharField: {'widget': Textarea}
    }


@admin.register(County)
class CountyAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    raw_id_fields = ('state_province',)


@admin.register(Record)
class RecordAdmin(DjangoObjectActions, admin.ModelAdmin):
    raw_id_fields = (
        'type', 'collection_code', 'basis_of_record', 'recorded_by', 'sex',
        'life_stage', 'occurrence_status', 'preparations', 'disposition',
        'sampling_protocol', 'habitat', 'water_body', 'locality',
        'identified_by', 'scientific_name', 'kingdom', 'phylum', '_class',
        'order', 'family', 'genus', 'specific_epithet', 'taxon_rank',
        'scientific_name_authorship', 'vernacular_name', 'nomenclatural_code',
        'taxonomic_status'
    )
    list_filter = ('collection_code',)
    fieldsets = (
        (_('Record Items'), {
            'fields': (
                'type', 'modified', 'language', 'license', 'rights_holder',
                'access_rights', 'bibliographic_citation', 'references',
                'institution_ID', 'collection_ID', 'dataset_ID',
                'institution_code', 'collection_code', 'dataset_name',
                'owner_institution_code', 'basis_of_record',
                'information_withheld', 'data_generalizations',
                'dynamic_properties'
            ),
        }),
        (_('Biological Record'), {
            'fields': (
                'occurrence_ID', 'catalog_number', 'occurrence_remarks',
                'record_number', 'recorded_by', 'organism_ID',
                'organism_quantity', 'organism_quantity_type', 'organism_name',
                'organism_scope', 'associated_organisms', 'organism_remarks',
                'individual_count', 'sex', 'life_stage',
                'reproductive_condition', 'behavior',
                'establishment_means', 'occurrence_status', 'preparations',
                'disposition', 'other_catalog_numbers',
                'previous_identifications', 'associated_media',
                'associated_references', 'associated_occurrences',
                'associated_sequences', 'associated_taxa', 'material_sample_ID'
            )
        }),
        (_('Event'), {
            'fields': (
                'event_ID', 'parent_event_ID', 'sampling_protocol',
                'sampling_effort', 'sampling_size_value', 'sampling_size_unit',
                'event_date', 'event_time', 'start_day_of_year',
                'end_day_of_year', 'year', 'month', 'day',
                'verbatim_event_date', 'habitat', 'field_number',
                'field_notes', 'event_remarks',
            )
        }),
        (_('Location'), {
            'fields': (
                'location_ID', 'higher_geography_ID', 'higher_geography',
                'continent', 'water_body', 'island_group',
                'island', 'locality', 'verbatim_elevation',
                'minimum_elevation_in_meters', 'maximum_elevation_in_meters',
                'verbatim_depth', 'minimum_depth_in_meters',
                'maximum_depth_in_meters',
                'minimum_distance_above_surface_in_meters',
                'maximum_distance_above_surface_in_meters',
                'location_according_to', 'location_remarks',
                'verbatim_coordinates', 'verbatim_latitude',
                'verbatim_longitude', 'verbatim_coordinate_system',
                'verbatim_SRS', 'decimal_latitude', 'decimal_longitude',
                'geodetic_datum', 'coordinate_uncertainty_in_meters',
                'coordinate_precision', 'point_radius_spatial_fit',
                'footprint_WKT', 'footprint_SRS', 'footprint_spatial_fit',
                'georeferenced_by', 'georeferenced_date',
                'georeference_protocol', 'georeference_sources',
                'georeference_verification_status', 'georeference_remarks'
            )
        }),
        (_('Geological Context'), {
            'fields': (
                'geological_context_ID', 'earliest_eon_or_lowest_eonothem',
                'latest_eon_or_highest_eonothem',
                'earliest_era_or_lowest_erathem',
                'latest_era_or_highest_erathem',
                'earliest_period_or_lowest_system',
                'latest_period_or_highest_system',
                'earliest_epoch_or_lowest_series',
                'latest_epoch_or_highest_series',
                'earliest_age_or_lowest_stage',
                'latest_age_or_highest_stage',
                'lowest_biostratigraphic_zone',
                'highest_biostratigraphic_zone', 'lithostratigraphic_terms',
                'group', 'formation', 'member', 'bed'
            )
        }),
        (_('Identification'), {
            'fields': (
                'identification_ID', 'identified_by', 'date_identified',
                'identification_references',
                'identification_verification_status', 'identification_remarks',
                'identification_qualifier', 'type_status'
            )
        }),
        (_('Taxon'), {
            'fields': (
                'taxon_ID', 'scientific_name_ID', 'accepted_name_usage_ID',
                'parent_name_usage_ID', 'original_name_usage_ID',
                'name_according_to_ID', 'name_published_in_ID',
                'taxon_concept_ID', 'scientific_name', 'accepted_name_usage',
                'parent_name_usage', 'original_name_usage',
                'name_according_to', 'name_published_in',
                'name_published_in_year', 'higher_classification', 'kingdom',
                'phylum', '_class', 'order', 'family', 'genus', 'subgenus',
                'specific_epithet', 'infraspecific_epithet', 'taxon_rank',
                'verbatim_taxon_rank', 'scientific_name_authorship',
                'vernacular_name', 'nomenclatural_code', 'taxonomic_status',
                'nomenclatural_status', 'taxon_remarks'
            )
        })
    )

    resource_class = RecordModelResource

    def export(self, request, queryset):
        app_label = self.opts.app_label
        model_name = self.opts.model_name
        ej = ExportJob.objects.create(
            app_label=app_label,
            model=model_name,
            site_of_origin=request.scheme + "://" + request.get_host(),
        )

        url = reverse(
            f'admin:{ej._meta.app_label}_{ej._meta.model_name}_change',
            args=[ej.pk]
        )
        return redirect(url)

    export.label = _('Export')
    export.short_description = _('Export with celery')

    changelist_actions = ['export']


MODELS = [Type, CollectionCode, BasisOfRecord, Sex, LifeStage,
          OccurrenceStatus, Preparation, Disposition, SamplingProtocol,
          Habitat, WaterBody, Country, StateProvince, Municipality, Locality,
          IdentifiedBy, ScientificName, Kingdom, Phylum, Class, Order, Family,
          Genus, SpecificEpithet, TaxonRank, ScientificNameAuthorship,
          VernacularName, NomenclaturalCode, TaxonomicStatus]


@admin.register(*MODELS)
class ListAndSearchImportExportModelAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

