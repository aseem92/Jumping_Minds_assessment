from django.urls import path
from elevator_system import views

urlpatterns = [
    path('initialize/<int:n>/', views.initialize_elevator_system, name='initialize'),
    path('requests/<int:elevator_id>/', views.fetch_all_requests, name='requests'),
    path('destination/<int:elevator_id>/', views.get_destination_floor, name='destination'),
    path('moving/<int:elevator_id>/', views.is_elevator_moving, name='moving'),
    path('request/', views.add_request, name='request'),
    path('maintenance/<int:elevator_id>/', views.mark_elevator_maintenance, name='maintenance'),
    path('door/<int:elevator_id>/', views.toggle_door, name='door'),
]
