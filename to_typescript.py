'''Handles the conversion of a json to a typescript type'''
from schemas import Schema
import os

OPEN_API_TYPES_IN_TS = {
    'string': 'string',
    'number': 'number',
    'integer': 'number',
    'boolean': 'boolean',
    'array': '[]',
    'object': '{}',
}

OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'


def convert_to_ts_interface(schema: Schema) -> list:
    '''Converts a json type to a typescript type'''
    interface = []
    interface.append(f'export interface {schema.name} {OPEN_BRACKET}')
    for proprety in schema.properties:
        interface.append(f'    {proprety.name}: {proprety.type};')

    interface.append(CLOSE_BRACKET)
    return interface


def write_ts_interface(interface: list, name: str) -> None:
    '''Writes a typescript interface to a file'''
    file_path = os.path.join('ts-interfaces', f'{name}.ts')
    print(file_path)
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in interface:
            file.write(f'{line}\n')
