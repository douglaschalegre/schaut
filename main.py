'''Transforming OPENAPI Schemas to Interfaces'''
import argparse
from schemas import Property, Schema
import openapi
import to_typescript

parser = argparse.ArgumentParser("simple_example")
parser.add_argument(
    "api", help="OpenAPI URL of project that serves as input to schemas creation", type=str)
parser.add_argument(
    "output", help="In what language will the output be in", type=str)

args = parser.parse_args()

schemas = openapi.get_schemas(openapi.request_openapi_data(
    args.api))

props_with_refs = {}
schema_classes = []
to_typescript.ts_mkdir()

for schema in schemas:
    schema_properties = openapi.get_schema_properties(schema)
    schema_required_properties = openapi.get_required_properties(schema)

    props: list[Property] = []
    for prop in schema_properties:
        props.append(Property.from_openapi_proprety(
            prop=prop,
            required=prop.name in schema_required_properties if prop.name else False
        ))

        if prop.items:
            if schema.title not in props_with_refs:
                props_with_refs[schema.title] = []
            props_with_refs[schema.title].append(props[-1])

    schema_class = Schema(name=schema.title, properties=props)
    schema_classes.append(schema_class)


for schema_class in schema_classes:
    if args.output == 'ts':
        interface = to_typescript.convert_to_ts_interface(schema_class)
        to_typescript.write_ts_interface(interface, schema_class.name)

if args.output == 'ts':
    for name, refs in props_with_refs.items():
        interface = to_typescript.update_interface_with_refs(
            name=name, props_with_refs=refs)
        to_typescript.write_ts_interface(interface, name)
