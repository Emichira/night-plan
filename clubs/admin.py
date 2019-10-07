from django.contrib import admin
from .models import Club
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin


class ClubAdmin(LeafletGeoAdmin):
    list_display = ('id', 'name', 'slug', 'updated_at', 'geometry', 'is_published')
    list_display_links = ('id', 'name')
    list_filter = ('county', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Club, ClubAdmin)