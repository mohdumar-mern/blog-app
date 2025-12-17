from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=75)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts',default=1)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    banner = models.ImageField(upload_to="posts/",default='fallback.png', blank=True)

    def __str__(self):
        return self.title

    # Optional: auto-generate slug if not provided
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
