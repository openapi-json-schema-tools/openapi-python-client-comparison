# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import openapi_client
from openapi_client.components.schema.user import User
from openapi_client.configurations import schema_configuration


class TestUser(unittest.TestCase):
    """User unit test stubs"""
    configuration_ = schema_configuration.SchemaConfiguration()


if __name__ == '__main__':
    unittest.main()
