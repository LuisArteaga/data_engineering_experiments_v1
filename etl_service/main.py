#!/usr/bin/env python3

import data_extraction_service.api_extraction as extract

# todo: Creating API Service
# todo: Creating Batch Processing Service for API
# todo: Creating Streaming Processing Service for API
# todo: Creating Webscraping Service

city = 'london'

dump = extract.get_current_weather_data(provider='openweathermap.org', city=city)

print(dump)