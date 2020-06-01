from django.db import models
from datetime import datetime
from drink_categories.models import DrinkCategory
from drink_glass_types.models import GlassType
from alcohol.models import Alcohol
from counties.models import County
from clubs.models import Club
from blogs.models import Blog
from django.urls import reverse
from django.utils.translation import activate

class Cocktail(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    cocktail_image = models.ImageField(upload_to='images/cocktail/%Y/%m/%d/')
    categories = models.ManyToManyField(DrinkCategory, null=True, blank=True)
    alcohol = models.ManyToManyField(Alcohol, null=True, blank=True)
    glass_type = models.ForeignKey(GlassType, on_delete=models.CASCADE, null=True, blank=True)
    blogs = models.ManyToManyField(Blog, null=True, blank=True)
    block_quote = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    cocktail_recipe_author = models.CharField(max_length=200, null=True, blank=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, blank=True, null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("slug", kwargs={"slug": self.slug })