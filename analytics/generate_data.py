import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django
import random
from datetime import datetime

# Django ko batana ki humein kaunsi settings use karni hai
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard_project.settings')
django.setup()

from analytics.models import Event

# Kuch sample pages aur event types
pages = ['/home', '/products', '/checkout', '/about', '/contact']
event_types = ['page_view', 'click', 'purchase', 'signup']

# 100 fake events banao
for i in range(100):
    Event.objects.create(
        user_id=f"user{random.randint(1, 20)}",
        event_type=random.choice(event_types),
        page=random.choice(pages),
    )

print("100 fake events created successfully!")