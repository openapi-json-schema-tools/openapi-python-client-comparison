# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client import api_client

from . import schema


class Parameter0(api_client.QueryParameter):
    name = "username"
    style = api_client.ParameterStyle.FORM
    schema = schema.Schema
    required = True
    explode = True
