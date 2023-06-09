# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.shared_imports.security_scheme_imports import *

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
