# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import openapi_client
from openapi_client.paths.pet_pet_id.delete import operation as delete  # noqa: E501
from openapi_client import schemas, api_client
from openapi_client.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestDelete(ApiTestMixin, unittest.TestCase):
    """
    Delete unit test stubs
        Deletes a pet  # noqa: E501
    """
    api_config = api_configuration.ApiConfiguration()
    schema_config = schema_configuration.SchemaConfiguration()
    used_api_client = api_client.ApiClient(configuration=api_config, schema_configuration=schema_config)
    api = delete.ApiForDelete(api_client=used_api_client)  # noqa: E501

    response_status = 400
    response_body = ''

if __name__ == '__main__':
    unittest.main()
