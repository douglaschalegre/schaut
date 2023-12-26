'''Handling OpenAPI data'''
import requests
from schemas import OpenApiProprety, OpenApiSchema


def request_openapi_data(url: str) -> requests.Response:
    '''Request OpenAPI data'''
    json_url = f'{url}/openapi.json'
    request = requests.get(json_url, timeout=500)

    if request.status_code != 200:
        raise ConnectionError(
            f'Error getting OpenAPI data: {request.status_code}')

    return request


def get_schemas(response: requests.Response) -> list[OpenApiSchema]:
    '''Get schemas from OpenAPI data'''
    schemas = response.json()['components']['schemas']

    if not schemas:
        raise ValueError('No schemas found in OpenAPI data')

    schemas_list: list[OpenApiSchema] = []
    for schema in schemas:
        properties = []
        if 'properties' in schemas[schema]:
            for proprety in schemas[schema]['properties']:
                properties.append(
                    OpenApiProprety(
                        name=proprety,
                        type=schemas[schema]['properties'][proprety]['type'] if 'type' in schemas[schema]['properties'][proprety] else None,
                        format=schemas[schema]['properties'][proprety]['format'] if 'format' in schemas[schema]['properties'][proprety] else None,
                        items=schemas[schema]['properties'][proprety]['items'] if 'items' in schemas[schema]['properties'][proprety] else None,
                    )
                )
        schemas_list.append(
            OpenApiSchema(
                title=schemas[schema]['title'],
                type=schemas[schema]['type'],
                description=schemas[schema]['description'] if 'description' in schemas[schema] else None,
                required=schemas[schema]['required'] if 'required' in schemas[schema] else None,
                properties=properties if properties else None,
                examples=schemas[schema]['examples'] if 'examples' in schemas[schema] else None,
                enum=schemas[schema]['enum'] if 'enum' in schemas[schema] else None,
                items=schemas[schema]['items'] if 'items' in schemas[schema] else None
            )
        )

    return schemas_list


def get_schemas_names(schemas: dict) -> list[str]:
    '''Get schemas names from OpenAPI data'''
    schemas_names = list(schemas.keys())

    if not schemas_names:
        raise ValueError('No schemas names found in OpenAPI data')

    return schemas_names


def get_schema_properties(schema: OpenApiSchema) -> list[OpenApiProprety]:
    '''Get schema properties from OpenAPI data'''
    properties = schema.properties

    if not properties:
        return []

    return properties


def get_required_properties(schema: OpenApiSchema) -> list[str]:
    '''Get schema required fields from OpenAPI data'''
    required = schema.required

    if not required:
        required = []

    return required


def get_optional_properties(schema_properties: dict, required_properties: list) -> list:
    '''Get schema optional fields from OpenAPI data'''
    optional = []
    for proprety in schema_properties:
        if proprety not in required_properties:
            optional.append(proprety)

    return optional
