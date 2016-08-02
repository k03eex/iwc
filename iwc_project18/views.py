from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse

from nodes import models

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')

def get_gps_json(request):
    jresponse = []
    nodes_gps = models.NodeGPS.objects.all()

    def get_values_dict(node_sensors):

        def get_list(node_sensors, sensor):
            parameter = []
            for i in node_sensors:
                parameter.append(i[sensor])
            return parameter

        temp = get_list(node_sensors, 'temperature')
        humidity = get_list(node_sensors, 'humidity')
        pressure = get_list(node_sensors, 'pressure')
        temp_max = max(temp)
        temp_min = min(temp)
        temp_avg = sum(temp)/len(temp)
        humidity_max = max(humidity)
        humidity_min = min(humidity)
        humidity_avg = sum(humidity)/len(humidity)
        pressure_max = max(pressure)
        pressure_min = min(pressure)
        pressure_avg = sum(pressure)/len(pressure)
        node_values_dict = {   'temp_max': temp_max,
                               'temp_min': temp_min,
                               'temp_avg': temp_avg,
                               'humidity_max': humidity_max,
                               'humidity_min': humidity_min,
                               'humidity_avg': humidity_avg,
                               'pressure_max': pressure_max,
                               'pressure_min': pressure_min,
                               'pressure_avg': pressure_avg
                            }
        return node_values_dict

    i = 1
    while i < 5:
        node_gps = nodes_gps.filter(node_id=i).latest('timestamp')
        node_sensors = models.Sensor.objects.filter(node_id=i).values()
        node_data = model_to_dict(node_gps)
        node_values = get_values_dict(node_sensors)
        node_data['values'] = node_values
        jresponse.append(node_data)
        i += 1

    print(jresponse)
    return JsonResponse(jresponse, safe=False)
