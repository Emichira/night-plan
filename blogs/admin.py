from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_author', 'is_published', 'blog_date')
    list_display_links = ('id', 'title')
    list_filter = ('categories', 'blog_date', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'blog_author', 'cocktail', 'alcohol',  'categories')
    list_per_page = 50

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)