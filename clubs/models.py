from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import activate
from counties.models import County
from django.utils.translation import activate
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db import models as geomodels

class Club(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True)
    club_image = models.ImageField(upload_to='static/img/clubs/%Y/%m/%d/')
    club_cover_image = models.ImageField(upload_to='images/event/%Y/%m/%d/', blank=True)
    reservation_number = models.CharField(max_length=200, null=True)
    description = models.TextField()
    location = models.CharField(max_length=200, null=True)
    geometry = geomodels.PointField(srid=4326, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("slug", kwargs={"slug": self.slug })