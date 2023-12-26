'''Transforming OPENAPI Schemas to Interfaces'''
import openapi
from schemas import Proprety, Schema
import to_typescript

schemas = openapi.get_schemas(openapi.request_openapi_data(
    'https://dev.subweb.com.br/tool/workflow/api'))


for schema in schemas:
    schema_properties = openapi.get_schema_properties(schema)
    schema_required_properties = openapi.get_required_properties(schema)

    propreties = []
    for proprety in schema_properties:
        object = proprety

        propreties.append(Proprety(
            required=proprety.name in schema_required_properties if proprety.name else False,
            type=proprety.type if proprety.type else None,
            name=proprety.name if proprety.name else None,
            format=proprety.format if proprety.format else None,
            items=proprety.items if proprety.items else None
        ))

    schema_class = Schema(name=schema.title, properties=propreties)
    interface = to_typescript.convert_to_ts_interface(schema_class)
    to_typescript.write_ts_interface(interface, schema_class.name)
