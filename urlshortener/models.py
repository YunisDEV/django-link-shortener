from django.db import models
from django.contrib.auth.models import User
from .utils import generateLink

# Create your models here.


class ShortedLink(models.Model):
    original_link = models.CharField(max_length=200)
    short_link = models.CharField(max_length=200, blank=True, null=True)
    owner = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_link:
            self.short_link = generateLink()
        return super().save(*args, **kwargs)
