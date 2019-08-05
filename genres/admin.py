from django.contrib import admin
from .models import Genre

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'name')
    list_filter = ('name','is_published')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Genre, GenreAdmin)