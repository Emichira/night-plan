from django.contrib import admin
from .models import BlogCategory

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 50

admin.site.register(BlogCategory, BlogCategoryAdmin)