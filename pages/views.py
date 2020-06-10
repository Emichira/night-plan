from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from cocktails.models import Cocktail
from drink_categories.models import DrinkCategory
from blogs.models import Blog
from events.models import Event
from event_types.models import EventType
from counties.models import County
from categories.models import Category
from clubs.models import Club
from drink_categories.models import DrinkCategory
from genres.models import Genre
from datetime import datetime, date
from django.db.models import Q

def home_page(request):
    brunch = Category.objects.filter(name='Brunch')
    editors = DrinkCategory.objects.filter(name='Editors')
    beers = DrinkCategory.objects.filter(name='Beer & Wine')
    flavors = DrinkCategory.objects.filter(name='Flavor')
    classic_cocktails = DrinkCategory.objects.filter(name='Classic Cocktails')
    classics = Cocktail.objects.filter(categories='1').order_by('-updated_at')
    top_rated = Cocktail.objects.filter(categories='2').order_by('-updated_at')
    editor = Cocktail.objects.filter(categories='3').order_by('-updated_at')
    beer_wine = Cocktail.objects.filter(categories='4').order_by('-updated_at')
    flavor = Cocktail.objects.filter(categories='5').order_by('-updated_at')
    brunch_events = Event.objects.filter(categories='7').order_by('event_date')
    posts = Blog.objects.filter(categories='1').order_by('-updated_at')
    trending = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    categories = Category.objects.all().order_by('name')

    context = {
        "brunchs" : brunch,
        'editor' : editor,
        'editors' : editors,
        'beer_wine' : beer_wine,
        'beers' : beers,
        'flavor' : flavor,
        'flavors' : flavors,
        'classics' : classics,
        'classic_cocktails' : classic_cocktails,
        'posts' : posts,
        "trending" : trending,
        'menu_cocktail_categories' : menu_cocktail_categories,
        'genres' : genres,
        "categories" : categories,
    }
    return render(request, "pages/index.html", context)

def explore_page(request):
    cover_image = Event.objects.filter(is_published=True).exclude(cover_image__isnull=True).exclude(cover_image__exact='').order_by('event_date')#display all cover images in detailed category
    clubs = Club.objects.filter(is_published=True).order_by('name')
    happy_hour = Event.objects.filter(categories='6', is_published=True).order_by('event_date')
    tonight = Event.objects.filter(event_date__date=date.today(), is_published=True)
    classics = Cocktail.objects.filter(categories='1').order_by('-updated_at')
    this_weekend = Event.objects.filter(Q(event_date__week_day=1) | Q(event_date__week_day=7), is_published=True)
    trending = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    categories = Category.objects.all().order_by('name')
    counties = County.objects.all().order_by('-created_at')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')

    context = {
        "covers" : cover_image,
        "clubs" : clubs,
        "happy_hour" : happy_hour,
        "tonight" : tonight,
        'classics' : classics,
        "this_weekend" : this_weekend,
        "trending" : trending,
        'genres' : genres,
        "categories" : categories,
        "counties" : counties,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "pages/explore.html", context)

def about_page(request):
    context = {
    }
    return render(request, "pages/about.html", context)

def terms_and_conditions_page(request):
    context = {
    }
    return render(request, "pages/terms-and-conditions.html", context)

def server_error(request):
    context = {
    }
    return render(request, 'pages/500.html', context)

def not_found(request, exception=None):
    context = {
    }
    return render(request, 'pages/404.html', context)

def permission_denied(request, exception=None):
    context = {
    }
    return render(request, 'pages/403.html', context)

def bad_request(request, exception=None):
    context = {
    }
    return render(request, 'pages/400.html', context)