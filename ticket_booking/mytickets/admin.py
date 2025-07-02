from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if change:
            # only update if you're storing extra fields in UserTicket
            obj.userticket_set.all().update()

admin.site.register(Ticket, TicketAdmin)
