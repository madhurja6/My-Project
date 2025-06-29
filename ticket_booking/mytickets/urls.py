from django.urls import path
from .import views

urlpatterns = [
    path('bookticket/<int:ticket_id>/', views.book_ticket_now, name='book_ticket_now'),
    path('my_tickets/', views.my_tickets, name='my_tickets'),
    path('cancelticket/<int:ticket_id>/', views.cancel_ticket, name='cancel_ticket'),
]
