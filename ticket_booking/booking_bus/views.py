from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from booking_bus.models import Ticketsbus
from mytickets.models import Ticket as MasterTicket, UserTicket

@login_required
def book_bus_ticket(request, ticket_id):
    original_ticket = get_object_or_404(Ticketsbus, id=ticket_id)

    # Create or get master ticket
    master_ticket, created = MasterTicket.objects.get_or_create(
        bus_ticket=original_ticket,
        defaults={
            'type': 'Bus',
            'source': original_ticket.source,
            'destination': original_ticket.destination,
            'departure_time': original_ticket.departure_time,
            'arrival_time': original_ticket.arrival_time,
            'total_seats': original_ticket.total_seats,
            'price': original_ticket.price,
        }
    )

    # Save user ticket if not already booked
    if not UserTicket.objects.filter(user=request.user, ticket=master_ticket).exists():
        UserTicket.objects.create(user=request.user, ticket=master_ticket)

    return redirect('booked')


# Create your views here.
def bushome(request):
    operators = [
        ("RedBus", "India’s largest online bus ticketing platform"),
        ("VRL Travels", "Trusted intercity bus operator across India"),
        ("SRS Travels", "Comfortable and reliable travel services"),
        ("KSRTC", "Government-run service with wide coverage"),
        ("Parveen Travels", "Luxury and AC coaches across South India"),
        ("Neeta Travels", "Popular choice for Western India routes")
    ]
    return render(request, 'booking_bus/bus_home.html', {'operators': operators})

def busbook(request):
    source = request.GET.get('source', '')
    destination = request.GET.get('destination', '')

    if source and destination:
        tickets = Ticketsbus.objects.filter(source__icontains=source, destination__icontains=destination)
    elif destination:
        tickets = Ticketsbus.objects.filter(destination__icontains=destination)
    elif source:
        tickets = Ticketsbus.objects.filter(source__icontains=source)
    else:
        tickets = Ticketsbus.objects.all()

    return render(request, 'booking_bus/book_bus.html', {'tickets': tickets})