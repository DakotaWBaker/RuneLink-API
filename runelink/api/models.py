from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser (AbstractUser):
    rsn = models.CharField(null = True, max_length= 12)

    def __str__(self):
        return self.username

class Child(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

class Tag(models.Model):
    title = models.CharField(max_length=255)

class Parent(models.Model): 
    title = models.CharField(max_length=255, null=True, blank=True)
    child = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)