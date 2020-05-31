from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.files.images import ImageFile
from events.models import Event
from categories.models import Category
from counties.models import County
from clubs.models import Club
from django.http import HttpResponse, Http404
from django.db.models import Q
from datetime import datetime, date
from genres.models import Genre

def blogs(request):
    #create objects
    #Handles displaying of all cocktails
    events = Event.objects.filter(is_published=True).order_by('event_date')
    categories = Category.objects.order_by('-created_at')
    #pagination of events
    paginator = Paginator(events, 3)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    genres = Genre.objects.filter(is_published=True).order_by('name')

    context = {
        "events" : paged_events,
        "categories" : categories,
        'genres' : genres,
    }
    return render(request, "blogs/blogs.html", context)

def blog(request, slug_blog):
    #create one detailed view object of a cocktail
    #Handles displaying of a single cocktail
    tonight = Event.objects.filter(event_date__date=date.today())
    event = get_object_or_404(Event, slug=slug_blog)
    genres = Genre.objects.filter(is_published=True).order_by('name')

    context = {
        "event" : event,
        "tonight" : tonight,
        'genres' : genres,
    }
    return render(request, "blogs/blog.html", context)

def search(request):
    #search based function for events, venue and counties
    queryset_event = Event.objects.order_by('event_date')
    query = request.GET.get('q')
    if query:
        queryset_event = queryset_event.filter(Q(title__icontains=query) |
        Q(venue__icontains=query) | Q(county__name__icontains=query)).distinct()
    cover_image = Event.objects.filter(is_published=True).order_by('event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    categories = Category.objects.order_by('-created_at')
    #pagination of rendered events
    paginator = Paginator(queryset_event, 16)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    genres = Genre.objects.filter(is_published=True).order_by('name')

    context = {
        "events" : paged_events,
        "categories" : categories,
        "covers" : cover_image,
        'genres' : genres,
    }
    return render(request, "events/search.html", context)