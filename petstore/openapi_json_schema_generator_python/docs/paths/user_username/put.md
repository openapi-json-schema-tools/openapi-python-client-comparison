openapi_client.paths.user_username.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| update_user | [UserApi](../../apis/tags/user_api.md) | This api is only for tag=user |
| put | ApiForPut | This api is only for this endpoint |
| put | UserUsername | This api is only for path=/user/{username} |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Security](#security)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Summary | Updated user |
| Description | This can only be done by the logged in user. |
| Path | "/user/{username}" |
| HTTP Method | put |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[body](#requestbody) | typing.Union[[RequestBody.content.application_json.schema](#RequestBody-content-applicationjson-schema), dict, frozendict.frozendict] | required |
[path_params](#path_params) | [RequestPathParameters.Params](#requestpathparametersparams), dict | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
server_index | typing.Optional[int] | default is None | Allows one to select a different server
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### RequestBody

#### Description
Updated user object

#### Content Type To Schema
Content-Type | Schema
------------ | -------
"application/json" | [content.application_json.Schema](#requestbody-content-applicationjson-schema)

#### RequestBody content ApplicationJson Schema

##### Type Info
Ref Class | Input Type | Accessed Type | Description
--------- | ---------- | ------------- | ------------
[User](../../components/schema/user.md) | dict, frozendict.frozendict | frozendict.frozendict |

### path_params
#### RequestPathParameters.Params
This is a TypedDict

Key | Input Type | Description  | Notes
------------- | ------------- | ------------- | -------------
username | [Parameter0.schema](#parameter0-schema), str | | 


#### Parameter0

##### Description
name that need to be deleted

##### Parameter0 Schema

###### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str | str |  |

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ResponseFor400.response_cls](#responsefor400-response_cls) | Invalid user supplied
404 | [ResponseFor404.response_cls](#responsefor404-response_cls) | User not found

## ResponseFor400

### Description
Invalid user supplied

### ResponseFor400 response_cls
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

## ResponseFor404

### Description
User not found

### ResponseFor404 response_cls
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

## Security

Set auth info by setting ApiConfiguration.security_scheme_info to a dict where the
key is the below security scheme quoted name, and the value is an instance of the linked
component security scheme class.
Select the security index by setting ApiConfiguration.security_index_info or by
passing in security_index into the endpoint method.
See how to do this in the code sample.
- these securities are specific to this to this endpoint

| Security Index | Security Scheme to Scope Names |
| -------------- | ------------------------------ |
| 0       | ["api_key"](../../components/security_schemes/security_scheme_api_key.md) []<br> |

## Servers

Set the available servers by defining your used servers in ApiConfiguration.server_info
Then select your server by setting a server index in ApiConfiguration.server_index_info or by
passing server_index in to the endpoint method.
- these servers are the general api servers
- defaults to server_index=0, server.url = http://petstore.swagger.io/v2

server_index | Class | Description
------------ | ----- | ------------
0 | [Server0](../../../servers/server_0.md) |

## Code Sample

```python
import openapi_client
from openapi_client.configurations import api_configuration
from openapi_client.apis.tags import user_api
from openapi_client.paths.user_username.put import operation
from pprint import pprint
# security_index 0
from openapi_client.components.security_schemes import security_scheme_api_key

# security_scheme_info for security_index 0
security_scheme_info: api_configuration.SecuritySchemeInfo = {
    "api_key": security_scheme_api_key.ApiKey(
        api_key='sampleApiKeyValue'
    ),
}

used_configuration = api_configuration.ApiConfiguration(
    security_scheme_info=security_scheme_info
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(used_configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    path_params: operation.RequestPathParameters.Params = {
        'username': "username_example",
    }
    body = user.User(
        id=1,
        username="username_example",
        first_name="first_name_example",
        last_name="last_name_example",
        email="email_example",
        password="password_example",
        phone="phone_example",
        user_status=1,
    )
    try:
        # Updated user
        api_response = api_instance.update_user(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```

[[Back to top]](#top)
[[Back to UserApi API]](../../apis/tags/user_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)