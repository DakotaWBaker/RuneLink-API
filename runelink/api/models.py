from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser (AbstractUser):
    rsn = models.CharField(null = True, max_length= 12)
    
    def __str__(self):
        return self.username

class SkillLevels (models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null = True, blank = True, related_name="skills")
    total = models.IntegerField(null = True, max_length=4)
    attack = models.IntegerField(null = True, max_length=4)
    defense = models.IntegerField(null = True, max_length=4)
    strength = models.IntegerField(null = True, max_length=4)
    hitpoints = models.IntegerField(null = True, max_length=4)
    ranged = models.IntegerField(null = True, max_length=4)
    prayer = models.IntegerField(null = True, max_length=4)
    magic = models.IntegerField(null = True, max_length=4)
    cooking = models.IntegerField(null = True, max_length=4)
    woodcutting = models.IntegerField(null = True, max_length=4)
    fletching = models.IntegerField(null = True, max_length=4)
    fishing = models.IntegerField(null = True, max_length=4)
    firemaking = models.IntegerField(null = True, max_length=4)
    crafting = models.IntegerField(null = True, max_length=4)
    smithing = models.IntegerField(null = True, max_length=4)
    mining = models.IntegerField(null = True, max_length=4)
    herblore = models.IntegerField(null = True, max_length=4)
    agility= models.IntegerField(null = True, max_length=4)
    thieving = models.IntegerField(null = True, max_length=4)
    slayer = models.IntegerField(null = True, max_length=4)
    farming = models.IntegerField(null = True, max_length=4)
    runecrafting = models.IntegerField(null = True, max_length=4)
    hunter = models.IntegerField(null = True, max_length=4)
    construction = models.IntegerField(null = True, max_length=4)

class GroupFinder(models.Model):
    body = models.CharField(null = True, max_length= 255)
    activity = models.CharField(null = True, max_length = 50)
    players_needed = models.IntegerField(null = True)
    time_posted = models.DateTimeField(auto_now_add= True, null = True)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null = True)

class GroupFinderComments(models.Model):
    comment = body = models.CharField(null = True, max_length= 255)
    post = models.ForeignKey(GroupFinder, on_delete = models.CASCADE, null = True)
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null = True)




class Child(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

class Tag(models.Model):
    title = models.CharField(max_length=255)

class Parent(models.Model): 
    title = models.CharField(max_length=255, null=True, blank=True)
    child = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)