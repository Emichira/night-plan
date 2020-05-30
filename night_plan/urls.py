"""night_plan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('pages.urls')),
    path('cocktails/', include('cocktails.urls')),
    path('blogs/', include('blogs.urls')),
    path('events/', include('events.urls')),
    path('events/categories/', include('categories.urls')),
    path('events/event_types/', include('event_types.urls')),
    path('county/', include('counties.urls')),
    path('accounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
    path('clubs/', include('clubs.urls')),
    path('genres/', include('genres.urls')),
    path('', include('google_analytics.urls')),
    path('admin/', admin.site.urls),
    # google adsense redirect configuration
    path('ads.txt', RedirectView.as_view(url=staticfiles_storage.url('ads.txt'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# error handling
handler404 = 'pages.views.not_found'
handler500 = 'pages.views.server_error'
handler403 = 'pages.views.permission_denied'
handler400 = 'pages.views.bad_request'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)