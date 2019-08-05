from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.TextField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
