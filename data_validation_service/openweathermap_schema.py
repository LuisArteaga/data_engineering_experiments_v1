#!/usr/bin/env python3

import json

def validate_json(json_data):
    try:
        json.loads(json_data)
    except ValueError as err:
        return False
    return True

def validate_data(raw_data, provider):
    if provider == 'openweathermap.org':
        if validate_json(json_data=raw_data):
            # Todo: Check for following schema
            # {'coord': {'lon': -0.1257, 'lat': 51.5085}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'base': 'stations', 'main': {'temp': 280.61, 'feels_like': 274.9, 'temp_min': 279.82, 'temp_max': 281.48, 'pressure': 1001, 'humidity': 66}, 'visibility': 10000, 'wind': {'speed': 5.66, 'deg': 240}, 'clouds': {'all': 40}, 'dt': 1615575313, 'sys': {'type': 1, 'id': 1414, 'country': 'GB', 'sunrise': 1615530077, 'sunset': 1615571961}, 'timezone': 0, 'id': 2643743, 'name': 'London', 'cod': 200}
            pass

