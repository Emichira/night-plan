from django.contrib import admin
from .models import Cocktail

class CocktailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cocktail_recipe_author', 'created_at', 'is_published')
    list_display_links = ('id', 'name')
    list_filter = ('alcohol', 'glass_type', 'categories', 'created_at', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('name', 'alcohol', 'categories''cocktail_recipe_author', 'club')
    list_per_page = 50

admin.site.register(Cocktail, CocktailAdmin)