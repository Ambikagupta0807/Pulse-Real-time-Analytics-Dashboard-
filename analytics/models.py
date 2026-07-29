from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ('page_view', 'Page View'),
        ('click', 'Click'),
        ('purchase', 'Purchase'),
        ('signup', 'Signup'),
    ]

    user_id = models.CharField(max_length=100)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    page = models.CharField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.user_id} - {self.event_type} - {self.timestamp}"