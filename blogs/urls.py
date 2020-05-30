from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<str:slug_event>/', views.blog, name='event'), #url using slug to display individual cocktail page
    path('search', views.search, name='search'), #url for search that handles search of cocktails
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)