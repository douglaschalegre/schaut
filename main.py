'''Transforming OPENAPI Schemas to Interfaces'''
import argparse
import openapi
import writter
from stratergy import TypescriptStrategy, strategy_factory
from schemas import Property, Schema

parser = argparse.ArgumentParser("simple_example")
parser.add_argument(
    "api", help="OpenAPI URL of project that serves as input to schemas creation", type=str)
parser.add_argument(
    "output", help="In what language will the output be in", type=str)

args = parser.parse_args()

STRATERGY = strategy_factory(args.output)

schemas = openapi.get_schemas(openapi.request_openapi_data(
    args.api))

props_with_refs = {}
schema_classes = []

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

writter.create_files(
    schema_classes=schema_classes,
    props_with_refs=props_with_refs,
    strategy=TypescriptStrategy()
)
