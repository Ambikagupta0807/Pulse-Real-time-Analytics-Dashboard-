from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.utils import timezone
from .models import Event

@receiver(post_save, sender=Event)
def event_created_handler(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()

        event_data = {
            'user_id': instance.user_id,
            'event_type': instance.event_type,
            'page': instance.page,
            'timestamp': timezone.localtime(instance.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
        }

        async_to_sync(channel_layer.group_send)(
            'dashboard_updates',
            {
                'type': 'send_update',
                'data': event_data,
            }
        )