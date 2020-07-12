from django.shortcuts import render, redirect, get_object_or_404
from cocktails.models import Cocktail
from .models import Alcohol
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, Http404
from drink_categories.models import DrinkCategory
from categories.models import Category
from genres.models import Genre

def category(request, slug_category):
    #handles display of cocktails belonging to a single category
    #slugify url
    category = get_object_or_404(Alcohol, slug=slug_category)
    alcohol_name = Alcohol.objects.get(slug=slug_category)
    # data to be displayed in filter section menu
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    event_categories = Category.objects.filter(name='Brunch').order_by('name')
    #display all cover images in detailed category
    #displays all cocktails with unique slug_category
    cocktails = Cocktail.objects.order_by('-created_at').filter(alcohol__slug=slug_category)
    paginator = Paginator(cocktails, 32)
    page = request.GET.get('page')
    paged_cocktails = paginator.get_page(page)

    context = {
        "event_categories" : event_categories,
        "name" : alcohol_name,
        "event_categories" : event_categories,
        "cocktails" : paged_cocktails,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "alcohols/alcohol-categories.html", context)