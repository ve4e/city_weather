from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        app_label = 'weather'


