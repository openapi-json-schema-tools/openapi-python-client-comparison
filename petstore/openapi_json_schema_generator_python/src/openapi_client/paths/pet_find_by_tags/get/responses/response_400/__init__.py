# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import dataclasses
import urllib3

from openapi_client import api_client
from openapi_client import schemas


@dataclasses.dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


class ResponseFor400(api_client.OpenApiResponse[ApiResponseFor400]):
    response_cls = ApiResponseFor400
