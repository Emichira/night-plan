from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('explore/', views.explore_page, name='explore'),
    path('about-us/', views.about_page, name='about'),
    path('terms&conditions/', views.terms_and_conditions_page, name='terms'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)