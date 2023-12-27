'''Schemas for the application'''
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class OpenApiProprety():
    '''Schema for openapi properties'''
    name: str
    type: str | None = field(default=None)
    format: str | None = field(default=None)
    items: dict | None = field(default=None)

    @staticmethod
    def from_request_data(data: dict, name: str) -> OpenApiProprety:
        '''Create a OpenApiProprety from request data'''
        return OpenApiProprety(
            name=name,
            type=data['type'] if 'type' in data else None,
            format=data['format'] if 'format' in data else None,
            items=data['items'] if 'items' in data else None
        )


@dataclass
class Proprety():
    '''Schema for properties'''
    required: bool
    type: str | None = field(default=None)
    name: str | None = field(default=None)
    format: str | None = field(default=None)
    items: dict | None = field(default=None)

    @staticmethod
    def from_openapi_proprety(prop: OpenApiProprety, required: bool) -> Proprety:
        '''Create a Proprety from OpenApiProprety'''
        return Proprety(
            required=required,
            type=prop.type,
            name=prop.name,
            format=prop.format,
            items=prop.items
        )


@dataclass
class Schema():
    '''Schema for schemas'''
    name: str
    properties: list[Proprety]


@dataclass
class OpenApiSchema():
    '''Schema for openapi schemas'''
    title: str
    type: str
    description: str | None = field(default=None)
    required: list[str] | None = field(default=None)
    properties: list[OpenApiProprety] | None = field(default=None)
    examples: list | None = field(default=None)
    enum: list | None = field(default=None)
    items: dict | None = field(default=None)

    @staticmethod
    def from_request_data(data: dict,
                          name: str,
                          properties: list[OpenApiProprety] | None) -> OpenApiSchema:
        '''Create a OpenApiSchema from request data'''
        return OpenApiSchema(
            title=name,
            type=data['type'],
            description=data['description'] if 'description' in data else None,
            required=data['required'] if 'required' in data else None,
            properties=properties if properties else None,
            examples=data['examples'] if 'examples' in data else None,
            enum=data['enum'] if 'enum' in data else None,
            items=data['items'] if 'items' in data else None
        )
