from django.contrib import admin

from .models import Member, Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'order')
    list_display_links = ('name',)
    search_fields = ('name',)
    readonly_fields = (
        'created_at', 'modified_at', 'created_by', 'modified_by'
    )
    list_editable = ('enabled',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_display_links = list_display
    search_fields = ('name',)
    readonly_fields = (
        'slug', 'created_at', 'modified_at', 'created_by', 'modified_by'
    )
