from django.db import models
from django.utils import timezone

class Tickets(models.Model):    
    seat_types = [
        ('BU','Business Class'),
        ('AC','AC Class'),
        ('SL','Sleeper Class'),
    ]

    seat_no = [
        ('BU','1-499'),
        ('AC','500-999'),
        ('SL','1000-1499'),
    ]

    name = models.CharField(max_length=20)
    date_time = models.DateTimeField(default=timezone.now)
    type1 = models.CharField(max_length=2, choices=seat_types)
    type2 = models.CharField(max_length=3, choices=seat_no)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    departure_time = models.DateTimeField(default=timezone.now)
    arrival_time = models.DateTimeField(default=timezone.now)
    total_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.source} to {self.destination})"

    