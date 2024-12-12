from django.contrib import admin
from django.utils.timezone import now
from contact.models import Contact


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'created_at', 
                    'response', 'response_sent_at', 'flag')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'created_at', 'message')
    list_filter = ('created_at', 'flag')
    
admin.site.register(Contact, ContactModelAdmin)