from django.db import models

class Elevator(models.Model):
    id = models.IntegerField(primary_key=True)
    current_floor = models.IntegerField(default=1)
    direction = models.CharField(max_length=10, default='STOP')
    is_available = models.BooleanField(default=True)
    is_operational = models.BooleanField(default=True)

    def __str__(self):
        return f'Elevator {self.id}'
