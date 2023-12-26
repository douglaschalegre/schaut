'''Transforming OPENAPI Schemas to Interfaces'''
import openapi
from schemas import Proprety, Schema
import to_typescript

schemas = openapi.get_schemas(openapi.request_openapi_data(
    'https://dev.subweb.com.br/tool/workflow/api'))

to_typescript.ts_mkdir()
for schema in schemas:
    schema_properties = openapi.get_schema_properties(schema)
    schema_required_properties = openapi.get_required_properties(schema)

    propreties = []
    for prop in schema_properties:
        propreties.append(Proprety(
            required=prop.name in schema_required_properties if prop.name else False,
            type=prop.type if prop.type else None,
            name=prop.name if prop.name else None,
            format=prop.format if prop.format else None,
            items=prop.items if prop.items else None
        ))

    schema_class = Schema(name=schema.title, properties=propreties)
    interface = to_typescript.convert_to_ts_interface(schema_class)
    to_typescript.write_ts_interface(interface, schema_class.name)
