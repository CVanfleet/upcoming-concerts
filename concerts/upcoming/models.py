from django.db import models

class CoPerformers(models.Model):
    band1 = models.CharField(max_length=100)
    band2 = models.CharField(max_length=100, null=True)
    band3 = models.CharField(max_length=100, null=True)


class Concert(models.Model):
    artist = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    performance_date = models.DateTimeField()
    coperformersId = models.ForeignKey(CoPerformers, on_delete=models.CASCADE, null=True)

    #def __str__(self):
    #    return self.artist