from django.db import models
from datetime import datetime
from categories.models import Category
from event_types.models import EventType
from counties.models import County
from clubs.models import Club
from genres.models import Genre
from django.urls import reverse
from django.utils.translation import activate
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db import models as geomodels

class Event(models.Model):
    categories = models.ManyToManyField(Category)
    event_type = models.ManyToManyField(EventType)
    county = models.ForeignKey(County, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True)
    event_image = models.ImageField(upload_to='images/event/%Y/%m/%d/')
    cover_image = models.ImageField(upload_to='images/event/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=200)
    event_date = models.DateTimeField(default=datetime.now)
    event_end_date = models.TimeField(default=datetime.now)
    venue = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)
    geometry = geomodels.PointField(srid=4326, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("slug", kwargs={"slug": self.slug })