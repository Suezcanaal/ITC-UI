from django.shortcuts import render
from django.http import JsonResponse
from .models import TrafficLog
from django.utils.timezone import localtime
import datetime

def index(request):
    directions = ['North', 'South', 'East', 'West']
    return render(request, 'index.html', {'directions': directions})

def run_simulation(request):
    def safe_int(value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return 0

    traffic = {
        'North': safe_int(request.GET.get('North')),
        'South': safe_int(request.GET.get('South')),
        'East': safe_int(request.GET.get('East')),
        'West': safe_int(request.GET.get('West')),
    }
    emergency = {
        'North': request.GET.get('ENorth') == 'on',
        'South': request.GET.get('ESouth') == 'on',
        'East': request.GET.get('EEast') == 'on',
        'West': request.GET.get('EWest') == 'on',
    }

    directions = sorted(traffic.keys(), key=lambda d: (not emergency[d], -traffic[d]))
    log = []

    for direction in directions:
        TrafficLog.objects.create(
            direction=direction,
            cars=traffic[direction],
            is_emergency=emergency[direction]
        )
        log.append({
            'direction': direction,
            'cars': traffic[direction],
            'priority': emergency[direction]
        })

    return JsonResponse({'sequence': log, 'timestamp': datetime.datetime.now().strftime("%H:%M:%S")})

def get_logs(request):
    logs = Log.objects.all().order_by('-timestamp')  # or whatever your log model is
    data = []
    for log in logs:
        data.append({
            'event': log.event,
            'timestamp': localtime(log.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
        })
    return JsonResponse({'logs': data})

    return JsonResponse({'logs': logs})