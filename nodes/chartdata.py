"""
from .models import Node


class ChartData(object):
    def get_data(nodeid):
        data = []
        valves = Node.objects.filter(nodeid=nodeid)

        for unit in valves:
            date = unit.timestamp
            aci = unit.aci
            data.append([date, aci])

        return data

        """
        data = {
            'timestamp': [],
            'aci': [],
            'temperature': [],
            'humidity': [],
            'pressure': [],
            'light': []
        }

        valves = Node.objects.filter(nodeid=nodeid)

        print(nodeid)

        for unit in valves:
            data['timestamp'].append(unit.timestamp)
            data['aci'].append(unit.aci)
            data['temperature'].append(unit.tempe)
            data['humidity'].append(unit.humidity)
            data['pressure'].append(unit.pressure)
            data['light'].append(unit.light)
        return data
        """
"""
