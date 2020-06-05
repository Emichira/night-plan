from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from cocktails.models import Cocktail
from blogs.models import Blog
from events.models import Event
from event_types.models import EventType
from counties.models import County
from categories.models import Category
from clubs.models import Club
from genres.models import Genre
from datetime import datetime, date
from django.db.models import Q

def home_page(request):
    brunch = Category.objects.all().filter(name='Brunch')
    editor = Cocktail.objects.all().filter(categories='5').order_by('-updated_at')
    beer_wine = Cocktail.objects.all().filter(categories='6').order_by('-updated_at')
    flavor = Cocktail.objects.all().filter(categories='4').order_by('-updated_at')
    classics = Cocktail.objects.all().filter(categories='1').order_by('-updated_at')
    posts = Blog.objects.all().filter(categories='1').order_by('-updated_at')
    trending = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')

    context = {
        "brunchs" : brunch,
        'editor' : editor,
        'beer_wine' : beer_wine,
        'flavor' : flavor,
        'classics' : classics,
        'posts' : posts,
        "trending" : trending,
    }
    return render(request, "pages/index.html", context)

def explore_page(request):
    cover_image = Event.objects.filter(is_published=True).exclude(cover_image__isnull=True).exclude(cover_image__exact='').order_by('event_date')#display all cover images in detailed category
    clubs = Club.objects.filter(is_published=True).order_by('name')
    happy_hour = Event.objects.filter(categories='6', is_published=True).order_by('event_date')
    tonight = Event.objects.filter(event_date__date=date.today(), is_published=True)
    this_weekend = Event.objects.filter(Q(event_date__week_day=1) | Q(event_date__week_day=7), is_published=True)
    trending = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    categories = Category.objects.all().order_by('name')
    counties = County.objects.all().order_by('-created_at')

    context = {
        "covers" : cover_image,
        "clubs" : clubs,
        "happy_hour" : happy_hour,
        "tonight" : tonight,
        "this_weekend" : this_weekend,
        "trending" : trending,
        'genres' : genres,
        "categories" : categories,
        "counties" : counties,
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
    cover_image = Event.objects.filter(is_published=True).exclude(cover_image__isnull=True).exclude(cover_image__exact='').order_by('event_date')#display all cover images in detailed category
    clubs = Club.objects.filter(is_published=True).order_by('name')
    happy_hour = Event.objects.filter(categories='6', is_published=True).order_by('event_date')
    tonight = Event.objects.filter(event_date__date=date.today(), is_published=True)
    this_weekend = Event.objects.filter(Q(event_date__week_day=1) | Q(event_date__week_day=7), is_published=True)
    trending = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    categories = Category.objects.all().order_by('name')
    counties = County.objects.all().order_by('-created_at')

    context = {
        "covers" : cover_image,
        "clubs" : clubs,
        "happy_hour" : happy_hour,
        "tonight" : tonight,
        "this_weekend" : this_weekend,
        "trending" : trending,
        'genres' : genres,
        "categories" : categories,
        "counties" : counties,
    }
    return render(request, 'pages/500.html', context)

def not_found(request, exception=None):
    cover_image = Event.objects.filter(is_published=True).exclude(cover_image__isnull=True).exclude(cover_image__exact='').order_by('event_date')#display all cover images in detailed category
    clubs = Club.objects.filter(is_published=True).order_by('name')
    happy_hour = Event.objects.filter(categories='6', is_published=True).order_by('event_date')
    tonight = Event.objects.filter(event_date__date=date.today(), is_published=True)
    this_weekend = Event.objects.filter(Q(event_date__week_day=1) | Q(event_date__week_day=7), is_published=True)
    trending = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    categories = Category.objects.all().order_by('name')
    counties = County.objects.all().order_by('-created_at')

    context = {
        "covers" : cover_image,
        "clubs" : clubs,
        "happy_hour" : happy_hour,
        "tonight" : tonight,
        "this_weekend" : this_weekend,
        "trending" : trending,
        'genres' : genres,
        "categories" : categories,
        "counties" : counties,
    }
    return render(request, 'pages/404.html', context)

def permission_denied(request, exception=None):
    cover_image = Event.objects.filter(is_published=True).exclude(cover_image__isnull=True).exclude(cover_image__exact='').order_by('event_date')#display all cover images in detailed category
    clubs = Club.objects.filter(is_published=True).order_by('name')
    happy_hour = Event.objects.filter(categories='6', is_published=True).order_by('event_date')
    tonight = Event.objects.filter(event_date__date=date.today(), is_published=True)
    this_weekend = Event.objects.filter(Q(event_date__week_day=1) | Q(event_date__week_day=7), is_published=True)
    trending = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    categories = Category.objects.all().order_by('name')
    counties = County.objects.all().order_by('-created_at')

    context = {
        "covers" : cover_image,
        "clubs" : clubs,
        "happy_hour" : happy_hour,
        "tonight" : tonight,
        "this_weekend" : this_weekend,
        "trending" : trending,
        'genres' : genres,
        "categories" : categories,
        "counties" : counties,
    }
    return render(request, 'pages/403.html', context)

def bad_request(request, exception=None):
    cover_image = Event.objects.filter(is_published=True).exclude(cover_image__isnull=True).exclude(cover_image__exact='').order_by('event_date')#display all cover images in detailed category
    clubs = Club.objects.filter(is_published=True).order_by('name')
    happy_hour = Event.objects.filter(categories='6', is_published=True).order_by('event_date')
    tonight = Event.objects.filter(event_date__date=date.today(), is_published=True)
    this_weekend = Event.objects.filter(Q(event_date__week_day=1) | Q(event_date__week_day=7), is_published=True)
    trending = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    categories = Category.objects.all().order_by('name')
    counties = County.objects.all().order_by('-created_at')

    context = {
        "covers" : cover_image,
        "clubs" : clubs,
        "happy_hour" : happy_hour,
        "tonight" : tonight,
        "this_weekend" : this_weekend,
        "trending" : trending,
        'genres' : genres,
        "categories" : categories,
        "counties" : counties,
    }
    return render(request, 'pages/400.html', context)