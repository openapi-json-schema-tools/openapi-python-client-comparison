# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from dataclasses import dataclass
import typing_extensions
import urllib3

from openapi_client import api_client, exceptions, security_schemes
import datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401

from .. import path
from .responses import response_default
from .security import security_requirement_object_0


_security: typing.List[security_schemes.SecurityRequirementObject] = [
    security_requirement_object_0.security_requirement_object,
]


default_response = response_default.Default


class BaseApi(api_client.Api):
    @typing.overload
    def _logout_user(
        self,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...

    @typing.overload
    def _logout_user(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _logout_user(
        self,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_default.Default.response_cls,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _logout_user(
        self,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Logs out current logged in user session
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            'servers', server_index
        )
        security_requirement_object = self.api_client.configuration.get_security_requirement_object(
            'paths/' + path + '/get/security',
            _security,
            security_index
        )

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get',
            host=host,
            security_requirement_object=security_requirement_object,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            api_response = default_response.deserialize(response, self.api_client.schema_configuration)

        if not 200 <= response.status <= 399:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class LogoutUser(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names

    @typing.overload
    def logout_user(
        self,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...

    @typing.overload
    def logout_user(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def logout_user(
        self,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_default.Default.response_cls,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def logout_user(
        self,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._logout_user(
            security_index=security_index,
            server_index=server_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForGet(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> response_default.Default.response_cls: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_default.Default.response_cls,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._logout_user(
            security_index=security_index,
            server_index=server_index,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


