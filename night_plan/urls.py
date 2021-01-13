from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('pages.urls')),
    path('cocktails/', include('cocktails.urls')),
    path('cocktails/alcohol_categories/', include('alcohol.urls')),
    path('cocktails/categories/', include('drink_categories.urls')),
    path('cocktails/glass_types/', include('drink_glass_types.urls')),
    path('blogs/', include('blogs.urls')),
    path('blogs/categories/', include('blog_categories.urls')),
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