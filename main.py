'''Transforming OPENAPI Schemas to Interfaces'''
import openapi
from schemas import Proprety, Schema
import to_typescript

schemas = openapi.get_schemas(openapi.request_openapi_data(
    'https://dev.subweb.com.br/tool/workflow/api'))
# print(schemas)


for schema in schemas:
    schema_properties = openapi.get_schema_properties(schema)
    schema_required_properties = openapi.get_required_properties(schema)

    propreties = []
    for proprety in schema_properties:
        print("####################")
        object = proprety
        print(object)
        # print(proprety.name,
        #       proprety.type,
        #       proprety.name,
        #       proprety.format,
        #       proprety.items)
        print("####################")

        # propreties.append(Proprety(
        #     required=proprety.name in schema_required_properties if proprety.name else False,
        #     type=proprety.type,
        #     name=proprety.name if proprety.name else None,
        #     format=proprety.format if proprety.format else None,
        #     items=proprety.items if proprety.items else None
        # ))

    # schema_class = Schema(name=schema.title, properties=schema_properties)
    # interface = to_typescript.convert_to_ts_interface(schema_class)
    # to_typescript.write_ts_interface(interface, schema_class.name)
