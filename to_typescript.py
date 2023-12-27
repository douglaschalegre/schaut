'''Handles the conversion of a json to a typescript type'''
import os
from schemas import Schema, Property

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
    for prop in schema.properties:
        line = interface_line(prop)
        if line is not None:
            interface.append(line)

    interface.append(CLOSE_BRACKET)
    return interface


def interface_line(prop: Property) -> str | None:
    '''Converts a prop to a typescript line'''
    if prop.type is None:
        return None
    symbol = '?' if not prop.required else ''
    return f'  {prop.name}{symbol}: {OPEN_API_TYPES_IN_TS[prop.type]};'


def interface_line_with_ref(ref: str, line: str, import_name: str) -> str:
    '''Converts an existing line into a line with a reference to another interface'''
    if '[]' in line:
        return line.replace('[]', f'{import_name}[]')
    return line.replace('{}', ref)


def write_ts_interface(interface: list, name: str) -> None:
    '''Writes a TypeScript interface to a file'''
    file_path = os.path.join('ts-interfaces', f'{name}.ts')
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in interface:
            file.write(f'{line}\n')


def update_interface_with_refs(name: str, props_with_refs: list[Property]) -> list[str]:
    '''Updates the interface with the references of other interfaces'''
    number_of_imports = 0
    new_interface = []
    with open(f'ts-interfaces/{name}.ts', 'r', encoding='utf-8') as file:
        for line in file:
            line_without_new_line = line.replace('\n', '')
            for prop in props_with_refs:
                if prop.name is not None and prop.name in line_without_new_line:
                    ref = prop.items.get(
                        '$ref', '') if prop.items is not None else ''
                    import_name = ref.split("/")[-1]
                    new_line = interface_line_with_ref(
                        ref=ref, line=line_without_new_line, import_name=import_name)
                    line_without_new_line = new_line
                    if ref != '':
                        new_interface.insert(
                            0, f'import {{ {import_name} }} from \'./{import_name}\';')
                        number_of_imports += 1
            new_interface.append(line_without_new_line)

    new_interface.insert(number_of_imports, '')
    return new_interface


def ts_mkdir() -> None:
    '''Creates the ts-interfaces folder'''
    if not os.path.exists('ts-interfaces'):
        os.mkdir('ts-interfaces')
