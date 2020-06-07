from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<str:slug_blog>/', views.blog, name='blog'), #url using slug to display individual cocktail page
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)