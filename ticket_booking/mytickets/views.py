from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Ticket, UserTicket

@login_required
def book_ticket_now(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Prevent double booking
    if UserTicket.objects.filter(user=request.user, ticket=ticket).exists():
        return redirect('my_tickets')

    # Save booking
    UserTicket.objects.create(user=request.user, ticket=ticket)
    return redirect('my_tickets')

def my_tickets(request):
    bookings = UserTicket.objects.filter(user=request.user)
    return render(request, 'mytickets/my_tickets.html', {
        'bookings': bookings,
        'now': timezone.now(),
    })


@login_required
def cancel_ticket(request, ticket_id):
    user_ticket = get_object_or_404(UserTicket, user=request.user, ticket_id=ticket_id)
    user_ticket.delete()
    return redirect('deleted')
