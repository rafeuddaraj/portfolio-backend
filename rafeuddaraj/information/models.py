from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    skills = models.TextField(blank=True)
    hero_image = models.URLField()
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    about = models.TextField()
    description = models.TextField()
    connect_with_me = models.TextField(blank=True)
    def __str__(self) -> str:
        return self.name