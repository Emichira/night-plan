from django.db import models
from datetime import datetime
from counties.models import County

class EventType(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name