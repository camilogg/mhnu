from django.contrib import admin

from .models import Slider, Member


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'enable', 'order')
    list_display_links = list_display
    search_fields = ('name',)
    readonly_fields = (
        'created_at', 'modified_at', 'created_by', 'modified_by'
    )


@admin.register(Member)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = list_display
    search_fields = ('name',)
    readonly_fields = (
        'created_at', 'modified_at', 'created_by', 'modified_by'
    )
