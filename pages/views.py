from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from cocktails.models import Cocktail
from alcohol.models import Alcohol
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
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home_page(request):
    brunch = Category.objects.filter(name='Brunch')
    vodka = Cocktail.objects.filter(alcohol__name='Vodka')
    whiskey = Cocktail.objects.filter(alcohol__name='Whiskey')
    gin = Cocktail.objects.filter(alcohol__name='Gin')
    rum = Cocktail.objects.filter(alcohol__name='Rum')
    tequila = Cocktail.objects.filter(alcohol__name='Tequila')
    beer_wine = Cocktail.objects.filter(categories__name='Beer & Wine').order_by('-updated_at')
    flavor = Cocktail.objects.filter(categories__name='Flavor').order_by('-updated_at')
    posts = Blog.objects.filter(categories='1').order_by('-updated_at')[:3]
    # data to be displayed in filter section menu
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')
    genres = Genre.objects.all().order_by('name').filter(is_published=True)
    event_categories = Category.objects.filter(name='Brunch').order_by('name')
    #   display all cocktails belonging to one category
    beers = DrinkCategory.objects.filter(name='Beer & Wine')
    vodka_cocktails = Alcohol.objects.filter(name='Vodka')
    whiskey_cocktails = Alcohol.objects.filter(name='Whiskey')
    gin_cocktails = Alcohol.objects.filter(name='Gin')
    rum_cocktails = Alcohol.objects.filter(name='Rum')
    tequila_cocktails = Alcohol.objects.filter(name='Tequila')
    flavors = DrinkCategory.objects.filter(name='Flavor')

    context = {
        "brunchs": brunch,
        'whiskey': whiskey,
        'vodka': vodka,
        'beer_wine': beer_wine,
        'gin': gin,
        'rum': rum,
        'tequila': tequila,
        'beers': beers,
        'flavor': flavor,
        'vodka_cocktails': vodka_cocktails,
        'posts': posts,
        'menu_cocktail_categories': menu_cocktail_categories,
        "event_categories": event_categories,
        'whiskey_cocktails': whiskey_cocktails,
        'gin_cocktails': gin_cocktails,
        'rum_cocktails': rum_cocktails,
        'tequila_cocktails': tequila_cocktails,
        'flavors': flavors,
    }
    return render(request, "pages/index.html", context)

def explore_page(request):
    #display all cover images in detailed category
    cover_image = Event.objects.filter(is_published=True).exclude(cover_image__isnull=True).exclude(cover_image__exact='').order_by('event_date')
    clubs = Club.objects.filter(is_published=True).order_by('name')
    happy_hour = Event.objects.filter(categories='6', is_published=True).order_by('event_date')
    tonight = Event.objects.filter(event_date__date=date.today(), is_published=True)
    classics = Cocktail.objects.filter(categories='1').order_by('-updated_at')
    this_weekend = Event.objects.filter(Q(event_date__week_day=1) | Q(event_date__week_day=7), is_published=True)
    trending = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    # data to be displayed in filter section menu
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    event_categories = Category.objects.filter(name='Brunch').order_by('name')
    counties = County.objects.all().order_by('-created_at')
    brunch_events = Event.objects.filter(categories='4').order_by('event_date')

    context = {
        "covers": cover_image,
        "clubs": clubs,
        "happy_hour": happy_hour,
        "tonight": tonight,
        'classics': classics,
        "this_weekend": this_weekend,
        "trending": trending,
        'genres': genres,
        "event_categories": event_categories,
        "counties": counties,
        'menu_cocktail_categories': menu_cocktail_categories,
        "brunch_events": brunch_events,
    }
    return render(request, "pages/explore.html", context)

def about_page(request):
    clubs = Club.objects.filter(is_published=True).order_by('name')

    context = {
        "clubs": clubs,
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