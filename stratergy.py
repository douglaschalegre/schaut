'''Stratergy pattern to implement different stratergies for the schema conversion'''
from abc import ABC, abstractmethod
import os
from schemas import Property, Schema
import to_typescript


class SchemaStratergy(ABC):
    '''Abstract class for schema conversion stratergies'''
    @abstractmethod
    def convert(self, schema: Schema):
        '''Converts a schema to a language specific interface'''
        pass

    @abstractmethod
    def write_references(self, schemas_with_references: dict[str, list[Property]]):
        '''Writes references on created schemas'''
        pass

    @abstractmethod
    def mkdir(self):
        '''Creates a path for the output(s)'''
        pass


class TypescriptStrategy(SchemaStratergy):
    '''Typescript schema conversion stratergy'''

    def convert(self, schema: Schema):
        interface = to_typescript.convert_to_ts_interface(schema)
        to_typescript.write_ts_interface(interface, schema.name)

    def write_references(self, schemas_with_references: dict[str, list[Property]]):
        for name, refs in schemas_with_references.items():
            interface = to_typescript.update_interface_with_refs(
                name=name, props_with_refs=refs)
            to_typescript.write_ts_interface(interface, name)

    def mkdir(self):
        if not os.path.exists('ts-interfaces'):
            os.mkdir('ts-interfaces')


def strategy_factory(output: str) -> SchemaStratergy:
    '''Factory for creating a stratergy'''
    if output == 'ts':
        return TypescriptStrategy()
    raise NotImplementedError('Invalid output type')
