# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.shared_imports.response_imports import *

from .content.application_xml import schema as application_xml_schema
from .content.application_json import schema as application_json_schema


@dataclasses.dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        application_xml_schema.Schema,
        application_json_schema.Schema,
    ]
    headers: schemas.Unset = schemas.unset


class ResponseFor200(api_client.OpenApiResponse[ApiResponseFor200]):
    response_cls = ApiResponseFor200


    class __ApplicationXmlMediaType(api_client.MediaType):
        schema: typing.Type[application_xml_schema.Schema] = application_xml_schema.Schema


    class __ApplicationJsonMediaType(api_client.MediaType):
        schema: typing.Type[application_json_schema.Schema] = application_json_schema.Schema
    __Content = typing_extensions.TypedDict(
        '__Content',
        {
            'application/xml': typing.Type[__ApplicationXmlMediaType],
            'application/json': typing.Type[__ApplicationJsonMediaType],
        }
    )
    content: __Content = {
        'application/xml': __ApplicationXmlMediaType,
        'application/json': __ApplicationJsonMediaType,
    }
