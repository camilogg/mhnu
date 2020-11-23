from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from .models import Record, Type, CollectionCode, BasisOfRecord, Sex, \
    LifeStage, OccurrenceStatus, Preparation, Disposition, RecordedBy, \
    SamplingProtocol, Habitat


@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(CollectionCode)
class CollectionCodeAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(BasisOfRecord)
class BasisOfRecordAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(RecordedBy)
class RecordedByAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(Sex)
class SexAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(LifeStage)
class LifeStageAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(OccurrenceStatus)
class OccurrenceStatusAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(Preparation)
class PreparationAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(Disposition)
class DispositionAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(SamplingProtocol)
class SamplingProtocolAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(Habitat)
class HabitatAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(Record)
class RecordAdmin(ImportExportModelAdmin):
    raw_id_fields = (
        'type', 'collection_code', 'basis_of_record', 'recorded_by', 'sex',
        'life_stage', 'occurrence_status', 'preparations', 'disposition',
        'sampling_protocol', 'habitat'
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
    )
