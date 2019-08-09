from django.shortcuts import render, get_object_or_404
from .models import County
from events.models import Event
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, Http404
from categories.models import Category

def county(request, slug_county):
    #create a detailed view of events in a county
    #Handles displaying of single county
    county = get_object_or_404(County, slug=slug_county)
    name = County.objects.get(slug=slug_county)
    events = Event.objects.order_by('-event_date').filter(county__slug=slug_county)
    cover_image = Event.objects.order_by('-event_date').exclude(cover_image__isnull=True).exclude(cover_image__exact='')
    paginator = Paginator(events, 16)
    page = request.GET.get('page')
    paged_events = paginator.get_page(page)
    categories = Category.objects.all().order_by('-created_at')

    context = {
        "county" : county,
        "counties" : name,
        "events" : paged_events,
        "covers" : cover_image,
        "categories" : categories,
    }
    return render(request, "counties/county.html", context)