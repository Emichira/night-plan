from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    #url using slug to display all cocktails page
    path('', views.cocktails, name='cocktails'),
    #url using slug to display individual cocktail page
    path('<str:slug_cocktail>/', views.cocktail, name='cocktail'),
    #url for search that handles search of cocktails, events and blogs
    path('search', views.search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)