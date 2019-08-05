from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from events.models import Event
from event_types.models import EventType
from counties.models import County
from categories.models import Category
from clubs.models import Club
from genres.models import Genre

def home_page(request):
    counties = County.objects.all()
    trending = Event.objects.all().order_by('-event_date').filter(event_type='1')
    featured = Event.objects.all().order_by('-event_date').filter(event_type='2')
    tonight = Event.objects.all().order_by('-event_date').filter(event_type='3')
    this_weekend = Event.objects.all().order_by('-event_date').filter(event_type='4')


    context = {
        "counties" : counties,
        "trending" : trending,
        "featured" : featured,
        "tonight" : tonight,
        "this_weekend" : this_weekend
    }
    return render(request, "pages/index.html", context)

def featured_city_page(request):
    cover_image = Event.objects.all().order_by('-event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='')#display all cover images in detailed category
    categories = Category.objects.all().order_by('-created_at')
    counties = County.objects.all().order_by('-created_at')
    clubs = Club.objects.all().order_by('-created_at').filter(is_published=True)
    genres = Genre.objects.all().order_by('-created_at').filter(is_published=True)
    trending = Event.objects.all().order_by('-event_date').filter(event_type='1')
    featured = Event.objects.all().order_by('-event_date').filter(event_type='2')
    tonight = Event.objects.all().order_by('-event_date').filter(event_type='3')
    this_weekend = Event.objects.all().order_by('-event_date').filter(event_type='4')
    this_week = Event.objects.all().order_by('-event_date').filter(event_type='5')
    just_for_you = Event.objects.all().order_by('-event_date').filter(event_type='6')


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
        "just_for_you" : just_for_you
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