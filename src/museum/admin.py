from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from .models import (
    Record, Type, CollectionCode, BasisOfRecord, Sex, LifeStage,
    OccurrenceStatus, Preparation, Disposition, RecordedBy, SamplingProtocol,
    Habitat, WaterBody, Country, StateProvince, County, Municipality, Locality
)


class ListAndSearchImportExportModelAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(CollectionCode)
class CollectionCodeAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(BasisOfRecord)
class BasisOfRecordAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(RecordedBy)
class RecordedByAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Sex)
class SexAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(LifeStage)
class LifeStageAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(OccurrenceStatus)
class OccurrenceStatusAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Preparation)
class PreparationAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Disposition)
class DispositionAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(SamplingProtocol)
class SamplingProtocolAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Habitat)
class HabitatAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(WaterBody)
class WaterBodyAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'country_code')
    search_fields = ('name',)


@admin.register(StateProvince)
class StateProvinceAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(County)
class CountyAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Municipality)
class MunicipalityAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Locality)
class LocalityAdmin(ImportExportModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Record)
class RecordAdmin(ImportExportModelAdmin):
    raw_id_fields = (
        'type', 'collection_code', 'basis_of_record', 'recorded_by', 'sex',
        'life_stage', 'occurrence_status', 'preparations', 'disposition',
        'sampling_protocol', 'habitat', 'water_body', 'locality',
    )
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
                'individual_count', 'sex', 'life_stage',
                'reproductive_condition', 'behavior',
                'establishment_means', 'occurrence_status', 'preparations',
                'disposition', 'other_catalog_numbers',
                'previous_identifications', 'associated_media',
                'associated_references', 'associated_occurrences',
                'associated_sequences', 'associated_taxa'
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
    )
