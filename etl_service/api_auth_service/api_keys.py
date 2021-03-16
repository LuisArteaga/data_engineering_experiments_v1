#!/usr/bin/env python3
import os

AUTH_DIRECTORY = './etl_service/api_auth_service/.auth'


class APIKeys:
    def __init__(self):
        self.folder = {'openweathermap.org': 'openweathermap.txt'}


def get_api_key(provider):
    api_keys = APIKeys()
    with open(os.path.join(AUTH_DIRECTORY, api_keys.folder[provider])) as f:
        api_key = f.read()

        return api_key
