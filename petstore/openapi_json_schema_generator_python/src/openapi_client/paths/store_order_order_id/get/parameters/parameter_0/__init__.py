# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.shared_imports.header_imports import *

from . import schema


class Parameter0(api_client.PathParameter):
    name = "orderId"
    style = api_client.ParameterStyle.SIMPLE
    schema = schema.Schema
    required = True
