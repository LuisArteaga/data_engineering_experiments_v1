#!/usr/bin/env python3


class SchemaColumns:
    def __init__(self):
        self.json_schema_keys = {"openweathermap.org": ['coord',
                                                        'weather',
                                                        'base',
                                                        'main',
                                                        'visibility',
                                                        'wind',
                                                        'clouds',
                                                        'dt',
                                                        'sys',
                                                        'timezone',
                                                        'id',
                                                        'name',
                                                        'cod'],
                                 "infura.io": ['data',
                                               'signature']
                                 }


def validate_json_data(raw_data, provider):
    try:
        validated_raw_data = raw_data.json()
    except ValueError:
        print('No JSON object could be decoded')

    schema_columns = SchemaColumns()

    if list(validated_raw_data.keys()) == schema_columns.json_schema_keys[provider]:
        return validated_raw_data
    else:
        raise Exception(f'{provider}: No valid schema. Column mismatch.')

