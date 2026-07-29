from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('summary/', views.analytics_summary, name='analytics_summary'),
    path('dashboard/', views.dashboard_page, name='dashboard_page'),
    path('track/', views.track_event, name='track_event'),
    path('demo/', views.demo_site, name='demo_site'),
]