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

    for schema in schemas:
        schemas[schema] = OpenApiSchema(**schemas[schema])
        print(type(schemas[schema]))

    return schemas


def get_schemas_names(schemas: dict) -> list[str]:
    '''Get schemas names from OpenAPI data'''
    schemas_names = list(schemas.keys())

    if not schemas_names:
        raise ValueError('No schemas names found in OpenAPI data')

    return schemas_names


def get_schema_properties(schema: OpenApiSchema) -> list[OpenApiProprety]:
    '''Get schema properties from OpenAPI data'''
    print(schema)
    properties = schema.properties

    if not properties:
        raise ValueError('No properties found in OpenAPI data')

    return properties


def get_required_properties(schema: OpenApiSchema) -> list:
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
