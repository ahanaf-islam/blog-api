from django.db import models
from datetime import datetime
from django.conf import settings


class BlogPost(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    blog_image = models.ImageField(upload_to='blog_image/%Y/%m/%d/', blank=False)
    content = models.TextField(blank=False)
    date_posted = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
