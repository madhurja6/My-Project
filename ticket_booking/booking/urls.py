from django.urls import path
from .import views

urlpatterns = [
    path('',views.trainhome,name='trainhome'),
    path('book/',views.book,name='book'),
    path('bookticket/<int:ticket_id>/', views.book_train_ticket, name='book_train_ticket'),
]