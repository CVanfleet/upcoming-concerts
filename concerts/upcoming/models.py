from django.db import models

class Concert(models.Model):
    artist = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    performance_date = models.DateTimeField()

class CoPerformers(models.Model):
    concertId = models.ForeignKey(Concert, on_delete=models.CASCADE)
    band = models.CharField(max_length=100)