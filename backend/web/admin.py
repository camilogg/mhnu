from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from tabbed_admin import TabbedModelAdmin

from .models import Slider, Member, Post, PostImage


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
        'created_at', 'modified_at', 'created_by', 'modified_by'
    )


class PostImageInline(admin.StackedInline):
    model = PostImage
    extra = 0
    readonly_fields = (
        'created_at', 'modified_at', 'created_by', 'modified_by'
    )


@admin.register(Post)
class PostAdmin(TabbedModelAdmin):
    list_display = ('name',)
    list_display_links = list_display
    search_fields = ('name',)
    readonly_fields = (
        'created_at', 'modified_at', 'created_by', 'modified_by'
    )
    tab_overview = (
        (None, {
            'fields': ('name', 'cover', 'summary', 'content')
        }),
    )
    tabs = [
        ('General', tab_overview),
        (_('Images'), (PostImageInline,)),
    ]
