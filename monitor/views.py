from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import psutil
import logging

# Setup logging
logging.basicConfig(
    filename='server_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_server_health():
    try:
        
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        server_health = {
            "cpu_usage": f"{cpu_usage}%",
            "memory": {
                "total": f"{memory.total / (1024 ** 3):.2f} GB",
                "used": f"{memory.used / (1024 ** 3):.2f} GB",
                "percent": f"{memory.percent}%"
            },
            "disk": {
                "total": f"{disk.total / (1024 ** 3):.2f} GB",
                "used": f"{disk.used / (1024 ** 3):.2f} GB",
                "percent": f"{disk.percent}%"
            }
        }

        

        logging.info("Successfully fetched server metrics.")
        return server_health

    except Exception as e:
        logging.error(f"Error fetching server metrics: {e}")
        return {"error": "Could not fetch server metrics."}
    

def health(request):
    return JsonResponse(get_server_health())

def home(request):
    context = get_server_health()
    return render(request, 'home.html', context)
