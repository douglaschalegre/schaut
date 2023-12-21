'''Schemas for the application'''
from dataclasses import dataclass, field


@dataclass
class OpenApiProprety():
    '''Schema for openapi properties'''
    name: str
    type: str
    format: str | None = field(default=None)
    items: dict | None = field(default=None)


@dataclass
class Proprety():
    '''Schema for properties'''
    required: bool
    name: str
    type: str
    format: str | None = field(default=None)
    items: dict | None = field(default=None)


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
