from django.db import models

# Create your models here.

class Speaker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.TextField()

class Accounts(models.Model):
    twitter = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    logo = models.ImageField()

class Venue(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    place = models.CharField(max_length=100)
    
# class Picture(models.Model):

class Event(models.Model):
    title = models.CharField(max_length=500)
    about = models.TextField()
    time = models.TimeField()
    date = models.DateField()

    speaker = models.ManyToManyField(Speaker)
    sponsor = models.ManyToManyField(Sponsor)
    venue = models.ManyToManyField(Venue)

