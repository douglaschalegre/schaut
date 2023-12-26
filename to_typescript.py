'''Handles the conversion of a json to a typescript type'''
import os
from schemas import Schema, Proprety

OPEN_API_TYPES_IN_TS = {
    'string': 'string',
    'number': 'number',
    'integer': 'number',
    'boolean': 'boolean',
    'array': '[]',
    'object': '{}',
    'None': 'any'
}

OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'


def convert_to_ts_interface(schema: Schema) -> list:
    '''Converts a json type to a typescript type'''
    interface = []
    interface.append(f'export interface {schema.name} {OPEN_BRACKET}')
    for proprety in schema.properties:
        line = interface_line(proprety)
        if line is not None:
            interface.append(line)

    interface.append(CLOSE_BRACKET)
    return interface


def interface_line(proprety: Proprety) -> str | None:
    '''Converts a proprety to a typescript line'''
    if proprety.type is None:
        return None
    symbol = '?' if not proprety.required else ''
    return f'    {proprety.name}{symbol}: {OPEN_API_TYPES_IN_TS[proprety.type]};'


def write_ts_interface(interface: list, name: str) -> None:
    '''Writes a typescript interface to a file'''
    ts_mkdir()
    file_path = os.path.join('ts-interfaces', f'{name}.ts')
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in interface:
            file.write(f'{line}\n')


def ts_mkdir() -> None:
    '''Creates the ts-interfaces folder'''
    if not os.path.exists('ts-interfaces'):
        os.mkdir('ts-interfaces')
