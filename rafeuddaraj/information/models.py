from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    skills = models.TextField(blank=True)
    hero_image = models.URLField()
    about = models.TextField()
    description = models.TextField()