from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from events.models import Event
from event_types.models import EventType
from counties.models import County
from categories.models import Category
from clubs.models import Club
from genres.models import Genre
from datetime import datetime, date
from django.db.models import Q

def home_page(request):
    counties = County.objects.all()
    trending = Event.objects.filter(event_type='1', is_published=True).order_by('event_date')
    happy_hour = Event.objects.filter(categories='6', is_published=True).order_by('event_date')
    featured = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    tonight = Event.objects.filter(event_date__date=date.today())
    this_weekend = Event.objects.filter(Q(event_date__week_day=1) | Q(event_date__week_day=7))
    weekend = this_weekend.order_by('event_date')
    clubs = Club.objects.filter(is_published=True).order_by('name')

    context = {
        "counties" : counties,
        "trending" : trending,
        "featured" : featured,
        "tonight" : tonight,
        "weekend" : weekend,
        "clubs" : clubs,
        "happy_hour" : happy_hour,
    }
    return render(request, "pages/index.html", context)

def featured_city_page(request):
    cover_image = Event.objects.filter(is_published=True).exclude(cover_image__isnull=True).exclude(cover_image__exact='').order_by('event_date')#display all cover images in detailed category
    categories = Category.objects.all().order_by('name')
    happy_hour = Event.objects.filter(categories='6', is_published=True).order_by('event_date')
    counties = County.objects.all().order_by('-created_at')
    clubs = Club.objects.filter(is_published=True).order_by('name')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    trending = Event.objects.filter(event_type='1', is_published=True).order_by('event_date')
    featured = Event.objects.filter(event_type='2', is_published=True).order_by('event_date')
    tonight = Event.objects.filter(event_date__date=date.today())
    this_weekend = Event.objects.filter(event_type='4', is_published=True).order_by('event_date')
    this_week = Event.objects.filter(event_type='5', is_published=True).order_by('event_date')
    just_for_you = Event.objects.filter(event_type='6', is_published=True).order_by('event_date')

    context = {
        "covers" : cover_image,
        "categories" : categories,
        "counties" : counties,
        "clubs" : clubs,
        'genres' : genres,
        "trending" : trending,
        "featured" : featured,
        "tonight" : tonight,
        "this_weekend" : this_weekend,
        "this_week" : this_weekend,
        "just_for_you" : just_for_you,
        "happy_hour" : happy_hour,
    }
    return render(request, "events/featured-city.html", context)

def about_page(request):
    context = {
    }
    return render(request, "pages/about.html", context)

def terms_and_conditions_page(request):
    context = {
    }
    return render(request, "pages/terms-and-conditions.html", context)

def faq_page(request):
    context = {
    }
    return render(request, "pages/faq.html", context)

def team_page(request):
    context = {
    }
    return render(request, "pages/team.html", context)