from django.db import models


class CulturalCenter(models.Model):
    name = models.CharField(max_length=200)
    poster = models.TextField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/cc')


class Event(models.Model):
    name = models.CharField(max_length=200)
    cultural_center = models.ForeignKey(CulturalCenter, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    ticket_link = models.URLField()
    image = models.ImageField(upload_to='images/e')
    going = models.BooleanField(default=False)
