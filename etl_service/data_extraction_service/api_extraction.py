#!/usr/bin/env python3

import etl_service.api_auth_service.api_keys as ak
import etl_service.data_validation_service.check_schema as owms
import requests


def get_current_weather_data(provider, city):
    if provider == 'openweathermap.org':
        api_key = ak.get_api_key(provider)
        raw_data = requests.get(url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
        raw_data_validated = owms.validate_json_data(raw_data=raw_data, provider=provider)

        return raw_data_validated
