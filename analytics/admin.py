from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'event_type', 'page', 'timestamp')
    list_filter = ('event_type',)
    search_fields = ('user_id', 'page')
