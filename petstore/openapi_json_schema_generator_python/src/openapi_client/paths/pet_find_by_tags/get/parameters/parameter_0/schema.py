# coding: utf-8

"""
    OpenAPI Petstore
    This is a sample server Petstore server. For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.shared_imports.schema_imports import *


class Schema(
    schemas.ListSchema
):


    class Schema_:
        types = {tuple}
        Items = schemas.StrSchema

    def __new__(
        cls,
        arg_: typing.Union[
            typing.Tuple[
                typing.Union[Schema_.Items, str], ...
            ],
            typing.List[
                typing.Union[Schema_.Items, str]
            ],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> 'Schema':
        return super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )

    def __getitem__(self, i: int) -> Schema_.Items:
        return super().__getitem__(i)
