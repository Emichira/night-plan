from django.shortcuts import render, get_object_or_404
from events.models import Event
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, Http404
from .models import Genre
from categories.models import Category

def genres(request):
    #create objects
    #Handles displaying of all genres
    genres = Genre.objects.all().order_by('name').filter(is_published=True)
    cover_image = Event.objects.all().order_by('event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    categories = Category.objects.all().order_by('-created_at')
    #pagination of genres to 16 per page
    paginator = Paginator(genres, 16)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)

    context = {
        "genres" : paged_events, #pass in 16 paginated genres per page to template
        "categories" : categories,
        "covers" : cover_image
    }
    return render(request, "genres/genres.html", context)

def genre(request, slug_genre):
    #create a detailed view of genres in a county
    #Handles displaying of a single category of a genre e.g Hip-hop or Reggae
    genre = get_object_or_404(Genre, slug=slug_genre)
    name = Genre.objects.get(slug=slug_genre)
    events = Event.objects.order_by('event_date').filter(genre__slug=slug_genre)
    cover_image = Event.objects.order_by('event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    paginator = Paginator(events, 16)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    categories = Category.objects.all().order_by('-created_at')
    genres = Genre.objects.all().order_by('name').filter(is_published=True)

    context = {
        "genre" : genre,
        "genres" : genres,
        "counties" : name,
        "events" : paged_events,
        "covers" : cover_image,
        "categories" : categories,
    }
    return render(request, "genres/genre.html", context)