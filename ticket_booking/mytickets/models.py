from django.db import models
from django.utils import timezone
from booking_plane.models import Ticketsplane
from booking.models import Tickets  # Train ticket
from booking_bus.models import Ticketsbus
from django.contrib.auth.models import User

class Ticket(models.Model):
    TICKET_TYPES = [
        ('Flight', 'Flight'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
    ]

    type = models.CharField(max_length=20, choices=TICKET_TYPES)
    plane_ticket = models.ForeignKey(Ticketsplane, on_delete=models.CASCADE, null=True, blank=True)
    train_ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, null=True, blank=True)
    bus_ticket = models.ForeignKey(Ticketsbus, on_delete=models.CASCADE, null=True, blank=True)

    date_time = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    total_seats = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.type}: {self.source} to {self.destination}"
    
class UserTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.ticket}"

