from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

# Sensor(title='temp_room1', description='kitchen')
class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
