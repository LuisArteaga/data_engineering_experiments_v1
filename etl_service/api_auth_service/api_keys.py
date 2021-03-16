#!/usr/bin/env python3

def get_api_key(provider):
    if provider == 'openweathermap.org':
        with open('./api_auth_service/.auth/openweathermap.txt') as f:
            api_key = f.read()

        return api_key
