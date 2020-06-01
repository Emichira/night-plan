from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import Event

class EventAdmin(LeafletGeoAdmin):
    list_display = ('id', 'title', 'venue', 'is_published', 'event_date', 'slug', 'county')
    list_display_links = ('id', 'title')
    list_filter = ('county', 'event_date', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'venue')
    list_per_page = 25

admin.site.register(Event, EventAdmin)