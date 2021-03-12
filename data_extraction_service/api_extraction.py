#!/usr/bin/env python3

import api_auth_service.api_keys as ak
import data_validation_service.openweathermap_schema as owms
import requests

def get_current_weather_data(provider, city):
    if provider == 'openweathermap.org':
        api_key = ak.get_api_key(provider)
        r = requests.get(url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
        raw_data = r.json()
        raw_data_validated = validate_data(raw_data=raw_data, provider=provider)
