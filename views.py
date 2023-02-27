from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Elevator

@csrf_exempt
def initialize_elevator_system(request, n):
    for i in range(n):
        Elevator.objects.create(id=i+1)
    return JsonResponse({'message': f'{n} elevators created.'})

@csrf_exempt
def fetch_all_requests(request, elevator_id):
    # Logic to fetch all requests for a given elevator
    return JsonResponse({'message': f'Requests for elevator {elevator_id}.'})

@csrf_exempt
def fetch_next_destination_floor(request, elevator_id):
    # Logic to fetch next destination floor for a given elevator
    return JsonResponse({'message': f'Next destination floor for elevator {elevator_id}.'})

@csrf_exempt
def fetch_elevator_direction(request, elevator_id):
    # Logic to fetch elevator direction for a given elevator
    return JsonResponse({'message': f'Direction of elevator {elevator_id}.'})

@csrf_exempt
def save_user_request(request, elevator_id, floor):
    # Logic to save user request for a given elevator and floor
    return JsonResponse({'message': f'User request saved for elevator {elevator_id} and floor {floor}.'})

@csrf_exempt
def mark_elevator_maintenance(request, elevator_id):
    # Logic to mark elevator as not working or in maintenance
    return JsonResponse({'message': f'Elevator {elevator_id} marked as not operational.'})

@csrf_exempt
def toggle_elevator_availability(request, elevator_id):
    # Logic to toggle elevator availability
    return JsonResponse({'message': f'Elevator {elevator_id} availability toggled.'})

@csrf_exempt
def toggle_elevator_running(request, elevator_id):
    # Logic to toggle elevator running status
    return JsonResponse({'message': f'Elevator {elevator_id} running status toggled.'})
