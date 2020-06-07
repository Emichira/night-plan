from django.db import models
from datetime import datetime
from counties.models import County

class GlassType(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    glass_image = models.ImageField(upload_to='images/cocktail/%Y/%m/%d/')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name