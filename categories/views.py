from django.shortcuts import render, redirect, get_object_or_404
from events.models import Event
from .models import Category
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, Http404
from genres.models import Genre

def category(request, slug_category):
    #handles display of events belonging to a single category
    category = Category.objects.filter(slug=slug_category) #slugify url
    if category.exists():
        category = category.first()
    else:
        raise Http404
    category_name = Category.objects.get(slug=slug_category)
    cover_image = Event.objects.order_by('event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='') #display all cover images in detailed category
    events = Event.objects.order_by('event_date').filter(categories__slug=slug_category) #displays all events with unique slug_category
    categories = Category.objects.all().order_by('-created_at')
    paginator = Paginator(events, 16)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    genres = Genre.objects.filter(is_published=True).order_by('name')

    context = {
        "category" : category,
        "name" : category_name,
        "categories" : categories,
        "events" : paged_events,
        'genres' : genres,
        "covers" : cover_image
    }
    return render(request, "categories/category.html", context)