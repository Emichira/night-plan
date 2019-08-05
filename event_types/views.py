from django.shortcuts import render, redirect

from .models import EventType

def index(request):
    eventtype = EventType.objects.all()
    context = {
        "events" : eventtype
    }
    return render(request, "events/featured-city.html", context)

def event(request):
    context = {
    }
    return render(request, "events/event.html", context)

def search(request):
    context = {
    }
    return render(request, "events/search.html", context)