from django.urls import path
from .import views

urlpatterns = [
    path('',views.bushome,name='bushome'),
    path('busbook/',views.busbook,name='busbook'),
    path('bookticket/<int:ticket_id>/', views.book_bus_ticket, name='book_bus_ticket'),
]