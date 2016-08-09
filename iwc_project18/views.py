#import necessary modules to work with JSON, Python dictionary
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse

#import models from nodes app
from nodes import models

def about(request):
    #return about template
    return render(request, 'about.html')

def home(request):
    #return index template
    return render(request, 'index.html')

def get_gps_json(request):
    '''function responses to AJAX request in JSON format'''
    jresponse = [] #initialize the variable
    nodes_gps = models.NodeGPS.objects.all() #get all objects from NodeGPS table

    def get_values_dict(node_sensors):
        '''get dictionary based data for each node sensor'''
        def get_list(node_sensors, sensor):
            '''convert list of objects into pure list which
            contains only one sensor parameter'''
            parameter = []
            for i in node_sensors:
                parameter.append(i[sensor])
            return parameter

        #get list of temp, humidity and pressure
        temp = get_list(node_sensors, 'temperature')
        humidity = get_list(node_sensors, 'humidity')
        pressure = get_list(node_sensors, 'pressure')
        #calcuate max, min and avg for each sensor parameters
        temp_max = max(temp)
        temp_min = min(temp)
        temp_avg = sum(temp)/len(temp)
        humidity_max = max(humidity)
        humidity_min = min(humidity)
        humidity_avg = sum(humidity)/len(humidity)
        pressure_max = max(pressure)
        pressure_min = min(pressure)
        pressure_avg = sum(pressure)/len(pressure)
        #add all values into dictionary to have structured data
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
        #loop to get the data for each node separately
        #get the last GPS data for a node
        node_gps = nodes_gps.filter(node_id=i).latest('timestamp')
        #get all objects from Sensor for a node
        node_sensors = models.Sensor.objects.filter(node_id=i).values()
        #convert model instance into python dictionary
        node_data = model_to_dict(node_gps)
        #get each sensor min, max and avg values in dinctionary format
        node_values = get_values_dict(node_sensors)
        #add sensor values to the main variable which contains GPS alsp
        node_data['values'] = node_values
        #append the overall data to the list
        jresponse.append(node_data)
        i += 1
    #response to request in JSON format
    return JsonResponse(jresponse, safe=False)
