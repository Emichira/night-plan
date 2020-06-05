from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # handles routing urls for a single glass type eg Pint or Martini Glass
    path('<str:slug_category>/', views.category, name='blogCategory'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)