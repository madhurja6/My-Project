from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from booking_plane.models import Ticketsplane
from mytickets.models import Ticket as MasterTicket, UserTicket

@login_required
def book_plane_ticket(request, ticket_id):
    original_ticket = get_object_or_404(Ticketsplane, id=ticket_id)

    # Create or get master ticket
    master_ticket, created = MasterTicket.objects.get_or_create(
        plane_ticket=original_ticket,
        defaults={
            'type': 'Flight',
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


def planehome(request):
    return render(request,'booking_plane/plane_home.html')

def planebook(request):
    source = request.GET.get('source', '')
    destination = request.GET.get('destination', '')

    if source and destination:
        tickets = Ticketsplane.objects.filter(source__icontains=source, destination__icontains=destination)
    elif destination:
        tickets = Ticketsplane.objects.filter(destination__icontains=destination)
    elif source:
        tickets = Ticketsplane.objects.filter(source__icontains=source)
    else:
        tickets = Ticketsplane.objects.all()

    return render(request, 'booking_plane/book_plane.html', {'tickets': tickets})