from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event
from cocktails.models import Cocktail
from .models import DrinkCategory
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, Http404
from genres.models import Genre
from categories.models import Category

def category(request, slug_category):
    #handles display of cocktails belonging to a single category
    #slugify url
    category = get_object_or_404(DrinkCategory, slug=slug_category)
    category_name = DrinkCategory.objects.get(slug=slug_category)
    # data to be displayed in filter section menu
    event_categories = Category.objects.filter(name='Brunch').order_by('name')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')
    #display all cover images in detailed category
    #displays all cocktails with unique slug_category
    cocktails = Cocktail.objects.order_by('-updated_at').filter(categories__slug=slug_category)
    paginator = Paginator(cocktails, 20)
    page = request.GET.get('page')
    paged_cocktails = paginator.get_page(page)
    genres = Genre.objects.filter(is_published=True).order_by('name')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')

    context = {
        "category" : category,
        "name" : category_name,
        "event_categories" : event_categories,
        "cocktails" : paged_cocktails,
        'genres' : genres,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "categories/cocktail-categories.html", context)