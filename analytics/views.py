from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Event
import pandas as pd
import json


def event_list(request):
    events = Event.objects.all().order_by('-timestamp')[:500]

    data = []
    for event in events:
        data.append({
            'user_id': event.user_id,
            'event_type': event.event_type,
            'page': event.page,
            'timestamp': timezone.localtime(event.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
        })

    return JsonResponse({'events': data})


def analytics_summary(request):
    events = Event.objects.all().values('user_id', 'event_type', 'page', 'timestamp')

    df = pd.DataFrame(list(events))

    if df.empty:
        return JsonResponse({'message': 'No data yet'})

    total_events = len(df)
    event_type_counts = df['event_type'].value_counts().to_dict()
    page_counts = df['page'].value_counts().to_dict()
    unique_users = df['user_id'].nunique()

    summary = {
        'total_events': total_events,
        'unique_users': unique_users,
        'event_type_breakdown': event_type_counts,
        'top_pages': page_counts,
    }

    return JsonResponse(summary)


def dashboard_page(request):
    return render(request, 'analytics/dashboard.html')

@csrf_exempt
def track_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Event.objects.create(
            user_id=data.get('user_id', 'demo_user'),
            event_type=data.get('event_type'),
            page=data.get('page'),
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def demo_site(request):
    return render(request, 'analytics/demo_site.html')