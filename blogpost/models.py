"""
from django.db import models
from datetime import datetime


class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False)
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
"""
