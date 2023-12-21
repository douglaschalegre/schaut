'''Transforming OPENAPI Schemas to Interfaces'''
import openapi
from schemas import Proprety, Schema
import to_typescript

schemas = openapi.get_schemas(openapi.request_openapi_data(
    'https://dev.subweb.com.br/tool/workflow/api'))
print(type(schemas))


# for schema in schemas:
# print(type(schema))
# schema_properties = openapi.get_schema_properties(schema)
# schema_required_properties = openapi.get_required_properties(schema)

# propreties = [
#     Proprety(
#         name=proprety.name,
#         type=proprety.type,
#         format=proprety.format,
#         items=proprety.items,
#         required=proprety.name in schema_required_properties)
#     for proprety in schema_properties if proprety.name in schema_required_properties]

# schema = Schema(name=schema.title, properties=schema_properties)
# interface = to_typescript.convert_to_ts_interface(schema)
# to_typescript.write_ts_interface(interface, schema.name)
