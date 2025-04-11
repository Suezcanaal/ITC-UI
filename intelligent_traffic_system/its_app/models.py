from django.db import models

class TrafficLog(models.Model):
    direction = models.CharField(max_length=10)
    cars = models.IntegerField()
    is_emergency = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direction} - {self.cars} cars - Emergency: {self.is_emergency}"