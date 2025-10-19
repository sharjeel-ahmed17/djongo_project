from django.shortcuts import render

def dashboard(request):
    edr_data = [
        {"edr_no": 4426467, "unit_id": 11052051, "batch": 223280, "rtc_time": "10/9/2025 2:41:23 AM",
         "di": 2, "ai": 33, "speed": 67.98, "x_value": 24.68, "y_value": 3,
         "gsm_signals": 428, "n_value": 169.7, "qty": "✓"},
        {"edr_no": 4426468, "unit_id": 11052051, "batch": 223280, "rtc_time": "10/9/2025 2:41:33 AM",
         "di": 2, "ai": 34, "speed": 67.99, "x_value": 24.68, "y_value": 3,
         "gsm_signals": 425, "n_value": 169.0, "qty": "✓"},
        {"edr_no": 4426468, "unit_id": 11052051, "batch": 223280, "rtc_time": "10/9/2025 2:41:33 AM",
         "di": 2, "ai": 34, "speed": 67.99, "x_value": 24.68, "y_value": 3,
         "gsm_signals": 425, "n_value": 169.0, "qty": "✓"},
        {"edr_no": 4426468, "unit_id": 11052051, "batch": 223280, "rtc_time": "10/9/2025 2:41:33 AM",
         "di": 2, "ai": 34, "speed": 67.99, "x_value": 24.68, "y_value": 3,
         "gsm_signals": 425, "n_value": 169.0, "qty": "✓"},
        {"edr_no": 4426468, "unit_id": 11052051, "batch": 223280, "rtc_time": "10/9/2025 2:41:33 AM",
         "di": 2, "ai": 34, "speed": 67.99, "x_value": 24.68, "y_value": 3,
         "gsm_signals": 425, "n_value": 169.0, "qty": "✓"},
        {"edr_no": 4426468, "unit_id": 11052051, "batch": 223280, "rtc_time": "10/9/2025 2:41:33 AM",
         "di": 2, "ai": 34, "speed": 67.99, "x_value": 24.68, "y_value": 3,
         "gsm_signals": 425, "n_value": 169.0, "qty": "✓"},
        # Add more sample rows or load from DB
    ]
    return render(request, 'blog/dashboard.html', {'edr_data': edr_data})
