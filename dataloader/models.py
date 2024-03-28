from django.db import models

class Eventdata(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(("event_name"),max_length=255)
    city_name = models.CharField(("city_name"),max_length=255)
    date  = models.DateField(("date"),auto_now = True)
    time = models.TimeField(("time"),auto_now = True)
    latitude = models.FloatField(("latitude"))
    longitude = models.FloatField(("longitude"))