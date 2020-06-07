from django.shortcuts import render, get_object_or_404
from events.models import Event
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, Http404
from .models import Club
from categories.models import Category
from genres.models import Genre
from drink_categories.models import DrinkCategory

def clubs(request):
    #create objects
    #Handles displaying of all clubs
    clubs = Club.objects.order_by('name').filter(is_published=True)
    cover_image = Event.objects.filter(is_published=True).exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    categories = Category.objects.order_by('-created_at')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    #pagination of events
    paginator = Paginator(clubs, 16)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')

    context = {
        "clubs" : paged_events,
        "categories" : categories,
        'genres' : genres,
        "covers" : cover_image,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "clubs/clubs.html", context)

def club(request, slug_club):
    #create a detailed view of events in a club
    #Handles displaying events of a single club
    club = get_object_or_404(Club, slug=slug_club)
    name = Club.objects.get(slug=slug_club)
    events = Event.objects.order_by('event_date').filter(club__slug=slug_club)
    cover_image = Event.objects.order_by('event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    paginator = Paginator(events, 16)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    categories = Category.objects.order_by('-created_at')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')

    context = {
        "club" : club,
        "counties" : name,
        "events" : paged_events,
        "covers" : cover_image,
        "categories" : categories,
        'genres' : genres,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "clubs/club.html", context)