from django.urls import path
from .import views

urlpatterns = [
    path('',views.planehome,name='planehome'),
    path('planebook/',views.planebook,name='planebook'),
    path('bookticket/<int:ticket_id>/', views.book_plane_ticket, name='book_plane_ticket'),
]