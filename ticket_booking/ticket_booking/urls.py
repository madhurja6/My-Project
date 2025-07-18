"""
URL configuration for ticket_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from.import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.login_user,name='login'),
    path('register/',views.register,name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('booked/', views.booked, name='booked'),
    path('payment/', views.payment, name='payment'),
    path('deleted/', views.deleted, name='deleted'),

    path('booking/',include('booking.urls')),
    path('busbooking/',include('booking_bus.urls')),
    path('planebooking/',include('booking_plane.urls')),
    path('mytickets/',include('mytickets.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
