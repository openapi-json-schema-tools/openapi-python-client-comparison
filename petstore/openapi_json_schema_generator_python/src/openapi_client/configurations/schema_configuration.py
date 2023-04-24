# coding: utf-8

"""
    OpenAPI Petstore

    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import typing

from openapi_client import exceptions


PYTHON_KEYWORD_TO_JSON_SCHEMA_KEYWORD = {
    'types': 'type',
    'enum_value_to_name': 'enum',
    'unique_items': 'uniqueItems',
    'min_items': 'minItems',
    'max_items': 'maxItems',
    'min_properties': 'minProperties',
    'max_properties': 'maxProperties',
    'min_length': 'minLength',
    'max_length': 'maxLength',
    'inclusive_minimum': 'minimum',
    'exclusive_minimum': 'exclusiveMinimum',
    'inclusive_maximum': 'maximum',
    'exclusive_maximum': 'exclusiveMaximum',
    'multiple_of': 'multipleOf',
    'regex': 'pattern',
    'format': 'format',
    'required': 'required',
    'items': 'items',
    'Items': 'items',
    'Properties': 'properties',
    'additional_properties': 'additionalProperties',
    'additionalProperties': 'additionalProperties',
    'OneOf': 'oneOf',
    'AnyOf': 'anyOf',
    'AllOf': 'allOf',
    '_not': 'not',
    '_Not': 'not',
    'discriminator': 'discriminator'
}

class SchemaConfiguration:
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator

    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    Do not edit the class manually.

    :param disabled_json_schema_keywords (set): Set of
      JSON schema validation keywords to disable JSON schema structural validation
      rules. The following keywords may be specified: multipleOf, maximum,
      exclusiveMaximum, minimum, exclusiveMinimum, maxLength, minLength, pattern,
      maxItems, minItems.
      By default, the validation is performed for data generated locally by the client
      and data received from the server, independent of any validation performed by
      the server side. If the input data does not satisfy the JSON schema validation
      rules specified in the OpenAPI document, an exception is raised.
      If disabled_json_schema_keywords is set, structural validation is
      disabled. This can be useful to troubleshoot data validation problem, such as
      when the OpenAPI document validation rules do not match the actual API data
      received by the server.
    :param server_index: Index to servers configuration.
    """

    def __init__(
        self,
        disabled_json_schema_keywords = frozenset(),
    ):
        """Constructor
        """
        self.disabled_json_schema_keywords = disabled_json_schema_keywords

    @property
    def disabled_json_schema_keywords(self) -> typing.Set[str]:
        return self.__disabled_json_schema_keywords

    @property
    def disabled_json_schema_python_keywords(self) -> typing.Set[str]:
        return self.__disabled_json_schema_python_keywords

    @disabled_json_schema_keywords.setter
    def disabled_json_schema_keywords(self, json_keywords: typing.Set[str]):
        disabled_json_schema_keywords = set()
        disabled_json_schema_python_keywords = set()
        for k in json_keywords:
            python_keywords = {key for key, val in PYTHON_KEYWORD_TO_JSON_SCHEMA_KEYWORD.items() if val == k}
            if not python_keywords:
                raise exceptions.ApiValueError(
                    "Invalid keyword: '{0}''".format(k))
            disabled_json_schema_keywords.add(k)
            disabled_json_schema_python_keywords.update(python_keywords)
        self.__disabled_json_schema_keywords = disabled_json_schema_keywords
        self.__disabled_json_schema_python_keywords = disabled_json_schema_python_keywords