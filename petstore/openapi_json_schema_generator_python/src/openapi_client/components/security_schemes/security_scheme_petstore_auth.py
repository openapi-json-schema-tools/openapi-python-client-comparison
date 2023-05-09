# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import dataclasses
import typing
import typing_extensions

from openapi_client import security_schemes

@dataclasses.dataclass
class PetstoreAuth(security_schemes.OAuth2SecurityScheme):
    flows = security_schemes.OAuthFlows(
        implicit=security_schemes.ImplicitOAuthFlow(
            authorization_url="http://petstore.swagger.io/api/oauth/dialog",
            scopes={
                "write:pets": "modify pets in your account",
                "read:pets": "read your pets",
            },
        )
    )
