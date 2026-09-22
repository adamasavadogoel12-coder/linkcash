from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')
    original_url = models.URLField()
    slug = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.slug} -> {self.original_url}"

class Click(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='clicks')
    clicked_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=2, blank=True, default="")
    device = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return f"Clic sur {self.link.slug} à {self.clicked_at}"
