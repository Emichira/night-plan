from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.files.images import ImageFile
from django.db.models import Q
from django.http import HttpResponse, Http404
from datetime import datetime, date
from .models import Cocktail
from drink_categories.models import DrinkCategory
from alcohol.models import Alcohol
from blog_categories.models import BlogCategory
from events.models import Event
from blogs.models import Blog
from categories.models import Category
from clubs.models import Club
from genres.models import Genre

def cocktails(request):
    #creates cocktail objects
    #Handles displaying of all cocktails
    cocktails = Cocktail.objects.all().order_by('-updated_at')
    # pull data for cocktail categories
    drink_categories = DrinkCategory.objects.all()[:6]
    #pagination of events
    paginator = Paginator(cocktails, 20)
    page = request.GET.get('page')
    paged_cocktails = paginator.get_page(page)
    blogcategories = BlogCategory.objects.all()[:6]
    # data to be displayed in filter section menu
    genres = Genre.objects.filter(is_published=True).order_by('name')[:6]
    event_categories = Category.objects.filter(name='Brunch').order_by('name')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')

    context = {
        "cocktails" : paged_cocktails,
        "drink_categories" : drink_categories,
        'blogcategories' : blogcategories,
        "event_categories" : event_categories,
        'genres' : genres,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "cocktails/cocktails.html", context)

def cocktail(request, slug_cocktail):
    #create one detailed view object of a cocktail
    #Handles displaying of a single cocktail
    cocktail = get_object_or_404(Cocktail, slug=slug_cocktail)
    top_rated_cocktails = Cocktail.objects.filter(categories="1")

    context = {
        "cocktail" : cocktail,
        'top_rated_cocktails' : top_rated_cocktails,
    }
    return render(request, "cocktails/cocktail.html", context)

def search(request):
    #search based function for events/cocktails/blogs based on venue and counties, alcohol, categories and blogs
    query = request.GET.get('q')
    queryset_cocktails = Cocktail.objects.order_by('-created_at')

    if query:
        # Look up Q objects for combining different fields in a single query
        queryset_cocktails = queryset_cocktails.filter(Q(name__icontains=query)).distinct()
    #pagination of rendered events
    paginator = Paginator(queryset_cocktails, 20)
    page = request.GET.get('page')
    paged_cocktails = paginator.get_page(page)
    cover_image = Event.objects.filter(is_published=True).order_by('event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    # pull data for cocktail categories
    drink_categories = DrinkCategory.objects.all()[:6]
    blogcategories = BlogCategory.objects.all()[:6]
    event_categories = Category.objects.filter(name='Brunch').order_by('name')
    genres = Genre.objects.filter(is_published=True).order_by('name')[:6]

    context = {
        "cocktails" : paged_cocktails,
        "drink_categories" : drink_categories,
        "covers" : cover_image,
        'blogcategories' : blogcategories,
        "event_categories" : event_categories,
        'genres' : genres,
    }
    return render(request, "cocktails/search.html", context)