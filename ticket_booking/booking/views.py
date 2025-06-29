from django.shortcuts import render, redirect, get_object_or_404
from .models import Tickets #train ticket model
from mytickets.models import Ticket as MasterTicket, UserTicket
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def book_train_ticket(request, ticket_id):
    original_ticket = get_object_or_404(Tickets, id=ticket_id)

    # Check if already exists in master Ticket model
    master_ticket, created = MasterTicket.objects.get_or_create(
        type='Train',
        train_ticket=original_ticket,
        defaults={
            'source': original_ticket.source,
            'destination': original_ticket.destination,
            'departure_time': original_ticket.departure_time,
            'arrival_time': original_ticket.arrival_time,
            'total_seats': original_ticket.total_seats,
            'price': original_ticket.price,
        }
    )

    if not UserTicket.objects.filter(user=request.user, ticket=master_ticket).exists():
        UserTicket.objects.create(user=request.user, ticket=master_ticket)

    return redirect('booked')

def trainhome(request):
    partners = [
        ("Indian Railways", "World’s fourth largest rail network connecting every corner of India"),
        ("IRCTC Tourism", "Government portal for booking trains, meals, and packages"),
        ("Konkan Railway", "Serving India's beautiful western coastal region"),
        ("Metro Rail Services", "Urban transport solution in metro cities like Delhi, Bengaluru"),
        ("Tejas Express", "Modern, high-speed luxury trains operated by IRCTC"),
        ("Vande Bharat Express", "India’s semi-high-speed flagship trains with top-class amenities"),
    ]
    return render(request, 'booking/trainhome.html', {'partners':partners})

def book(request):
    source = request.GET.get('source', '')
    destination = request.GET.get('destination', '')

    if source and destination:
        tickets = Tickets.objects.filter(source__icontains=source, destination__icontains=destination)
    elif destination:
        tickets = Tickets.objects.filter(destination__icontains=destination)
    elif source:
        tickets = Tickets.objects.filter(source__icontains=source)
    else:
        tickets = Tickets.objects.all()

    return render(request, 'booking/book.html', {'tickets': tickets})


