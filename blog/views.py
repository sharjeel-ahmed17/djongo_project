from django.shortcuts import render
from .models import DashboardItem

def dashboard(request):
    # items = DashboardItem.objects.all().order_by('-created_at')
    edr_data = [
        {"edr_no": 4426467, "unit_id": 11052051, "batch": 223280, "rtc_time": "10/9/2025 2:41:23 AM", "di": 2, "ai": 33,
         "speed": 67.98, "x_value": 24.68, "y_value": 3, "gsm_signals": 428, "n_value": 169.7, "qty": "✓"},
    ]
    return render(request, 'blog/dashboard.html', {'edr_data': edr_data})




# def edr_dashboard(request):
#     # example static data (replace with queryset or API data)
#     edr_data = [
#         {"edr_no": 4426467, "unit_id": 11052051, "batch": 223280, "rtc_time": "10/9/2025 2:41:23 AM", "di": 2, "ai": 33,
#          "speed": 67.98, "x_value": 24.68, "y_value": 3, "gsm_signals": 428, "n_value": 169.7, "qty": "✓"},
#     ]
#     return render(request, 'edr_dashboard.html', {'edr_data': edr_data})
