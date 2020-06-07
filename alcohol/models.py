from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import activate

class Alcohol(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    alcohol_image = models.ImageField(upload_to='images/alcohol/%Y/%m/%d/')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("slug", kwargs={"slug": self.slug })

    class Meta:
        verbose_name_plural = "alcohols"