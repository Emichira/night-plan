from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.files.images import ImageFile
from .models import Blog, Comment
from .forms import CommentForm
from cocktails.models import Cocktail
from events.models import Event
from categories.models import Category
from blog_categories.models import BlogCategory
from counties.models import County
from clubs.models import Club
from django.http import HttpResponse, Http404
from django.db.models import Q
from datetime import datetime, date
from genres.models import Genre
from drink_categories.models import DrinkCategory

def blogs(request):
    #create objects
    #Handles displaying of all blogs
    posts = Blog.objects.all().order_by('blog_date')
    brunch = Category.objects.all().filter(name='Brunch')
    #pagination of blogs
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    cocktails = Cocktail.objects.filter(categories="2")[:3]
    categories = Category.objects.order_by('-created_at')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')

    context = {
        'posts' : paged_posts,
        'cocktails' : cocktails,
        "categories" : categories,
        'genres' : genres,
        "brunchs" : brunch,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "blogs/blogs.html", context)

def blog(request, slug_blog):
    #create one detailed view object of a cocktail
    #Handles displaying of a single blog post
    blog = get_object_or_404(Blog, slug=slug_blog)
    top_rated_cocktails = Cocktail.objects.filter(categories="1")
    cocktails = Cocktail.objects.filter(categories="4")[:3]
    categories = Category.objects.order_by('-created_at')
    genres = Genre.objects.filter(is_published=True).order_by('name')
    brunch = Category.objects.all().filter(name='Brunch')
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')
    form = CommentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.instance.blog = blog
            form.save()
            return redirect(reverse('blog', kwargs={
                'slug_blog': blog.slug
            }))

    context = {
        "blog" : blog,
        'top_rated_cocktails' : top_rated_cocktails,
        'cocktails' : cocktails,
        "categories" : categories,
        'genres' : genres,
        "brunchs" : brunch,
        'menu_cocktail_categories' : menu_cocktail_categories,
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
    menu_cocktail_categories = DrinkCategory.objects.all().order_by('-created_at')

    context = {
        "events" : paged_events,
        "categories" : categories,
        "covers" : cover_image,
        'genres' : genres,
        'menu_cocktail_categories' : menu_cocktail_categories,
    }
    return render(request, "events/search.html", context)