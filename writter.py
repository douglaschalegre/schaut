'''File responsible for writting the output files'''

from schemas import Property, Schema
from stratergy import SchemaStratergy


def create_files(
        schema_classes: list[Schema],
        props_with_refs: dict[str, list[Property]],
        strategy: SchemaStratergy
):
    '''Creates files based on the schema classes and the stratergy choosen'''
    strategy.mkdir()
    for schema_class in schema_classes:
        strategy.convert(schema_class)

    strategy.write_references(props_with_refs)
