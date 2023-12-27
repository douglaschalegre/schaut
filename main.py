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
        propreties.append(Proprety.from_openapi_proprety(
            prop=prop,
            required=prop.name in schema_required_properties if prop.name else False
        ))

    schema_class = Schema(name=schema.title, properties=propreties)
    interface = to_typescript.convert_to_ts_interface(schema_class)
    to_typescript.write_ts_interface(interface, schema_class.name)
