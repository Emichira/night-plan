from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import activate

class BlogCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    blog_category_image = models.ImageField(upload_to='images/blog/%Y/%m/%d/')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("slug", kwargs={"slug": self.slug })

    class Meta:
        verbose_name_plural = "categories"