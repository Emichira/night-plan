from django.db import models
from datetime import datetime
from blog_categories.models import BlogCategory
from drink_categories.models import DrinkCategory
from drink_glass_types.models import GlassType
from cocktails.models import Cocktail
from alcohol.models import Alcohol
from django.urls import reverse
from django.utils.translation import activate

class Blog(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    blog_image = models.ImageField(upload_to='images/blog/%Y/%m/%d/')
    short_description = models.CharField(max_length=66)
    first_paragraph = models.TextField()
    middle_paragragh = models.TextField(null=True, blank=True)
    final_paragragh = models.TextField(null=True, blank=True)
    blog_author = models.CharField(max_length=200, blank=True, null=True)
    categories = models.ManyToManyField(BlogCategory, blank=True)
    cocktail = models.ManyToManyField(Cocktail, blank=True)
    drink_categories = models.ForeignKey(DrinkCategory, on_delete=models.CASCADE, blank=True, null=True)
    glass_type = models.ForeignKey(GlassType, on_delete=models.CASCADE, blank=True, null=True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, blank=True, null=True)
    county = models.CharField(max_length=200, blank=True, null=True)
    reading_time = models.CharField(max_length=2, blank=True, null=True)
    blog_date = models.DateField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("slug", kwargs={"slug": self.slug })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(blog=self).count()

    @property
    def view_count(self):
        return Blog.objects.filter(blog=self).count()

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    blog = models.ForeignKey(
        'Blog', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name