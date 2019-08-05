from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import activate
from counties.models import County

class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    genre_image = models.ImageField(upload_to='static/img/genre/%Y/%m/%d/')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("slug", kwargs={"slug": self.slug })