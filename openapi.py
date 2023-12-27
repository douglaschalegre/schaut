'''Handling OpenAPI data'''
import requests
from schemas import OpenApiProperty, OpenApiSchema


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

    key_list = get_schemas_names(schemas)

    schemas_list: list[OpenApiSchema] = []
    for schema in schemas:
        index = key_list.index(schema)
        key = key_list[index]

        properties = []
        if 'properties' in schemas[schema]:
            for prop in schemas[schema]['properties']:
                properties.append(
                    OpenApiProperty.from_request_data(
                        data=schemas[schema]['properties'][prop], name=prop))

        schemas_list.append(
            OpenApiSchema.from_request_data(
                data=schemas[schema], name=key, properties=properties))

    return schemas_list


def get_schemas_names(schemas: dict) -> list[str]:
    '''Get schemas names from OpenAPI data'''
    schemas_names = list(schemas.keys())

    if not schemas_names:
        raise ValueError('No schemas names found in OpenAPI data')

    return schemas_names


def get_schema_properties(schema: OpenApiSchema) -> list[OpenApiProperty]:
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
    for prop in schema_properties:
        if prop not in required_properties:
            optional.append(prop)

    return optional
