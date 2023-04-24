openapi_client.paths.user_login.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| login_user | [UserApi](../../apis/tags/user_api.md) | This api is only for tag=user |
| get | ApiForGet | This api is only for this endpoint |
| get | UserLogin | This api is only for path=/user/login |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Summary | Logs user into the system |
| Path | "/user/login" |
| HTTP Method | get |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[query_params](#query_params) | [RequestQueryParameters.Params](#requestqueryparametersparams), dict | |
accept_content_types | typing.Tuple[str] | default is ("application/xml", "application/json", ) | Tells the server the content type(s) that are accepted by the client
server_index | typing.Optional[int] | default is None | Allows one to select a different server
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParameters.Params
This is a TypedDict

Key | Input Type | Description  | Notes
------------- | ------------- | ------------- | -------------
username | [Parameter0.schema](#parameter0-schema), str | | 
password | [Parameter1.schema](#parameter1-schema), str | | 


#### Parameter0

##### Description
The user name for login

##### Parameter0 Schema

###### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str | str |  |

#### Parameter1

##### Description
The password for login in clear text

##### Parameter1 Schema

###### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str | str |  |

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ResponseFor200.response_cls](#responsefor200-response_cls) | successful operation
400 | [ResponseFor400.response_cls](#responsefor400-response_cls) | Invalid username/password supplied

## ResponseFor200

### Description
successful operation

### ResponseFor200 response_cls
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
[body](#responsefor200-body) | typing.Union[[content.application_xml.schema](#responsefor200-content-applicationxml-schema), [content.application_json.schema](#responsefor200-content-applicationjson-schema)] |  |
[headers](#headers) | [Headers](#headers) |  |

### ResponseFor200 Body
Content-Type | Schema
------------ | -------
"application/xml" | [content.application_xml.Schema](#responsefor200-content-applicationxml-schema)
"application/json" | [content.application_json.Schema](#responsefor200-content-applicationjson-schema)

### Headers
Key | Accessed Type | Description  | Notes
------------- | ------------- | ------------- | -------------
X-Rate-Limit | [headers.header_x_rate_limit.schema](#responsefor200-headers-xratelimit-schema) | | optional
X-Expires-After | [headers.header_x_expires_after.schema](#responsefor200-headers-xexpiresafter-schema) | | optional
Set-Cookie | [headers.header_set_cookie.schema](#responsefor200-headers-setcookie-schema) | | optional

### Body Details
#### ResponseFor200 content ApplicationXml Schema

##### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str | str |  |
#### ResponseFor200 content ApplicationJson Schema

##### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str | str |  |

### Header Details
#### ResponseFor200 headers XRateLimit

##### Description
calls per hour allowed by the user

##### ResponseFor200 headers XRateLimit Schema

###### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int | decimal.Decimal |  | value must be a 32 bit integer
#### ResponseFor200 headers XExpiresAfter

##### Description
date in UTC when token expires

##### ResponseFor200 headers XExpiresAfter Schema

###### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime.datetime | str |  | value must conform to RFC-3339 date-time
#### ResponseFor200 headers SetCookie

##### Description
Cookie authentication key for use with the &#x60;api_key&#x60; apiKey authentication.

##### ResponseFor200 headers SetCookie Schema

###### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str | str |  |

## ResponseFor400

### Description
Invalid username/password supplied

### ResponseFor400 response_cls
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

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
from openapi_client.paths.user_login.get import operation
from pprint import pprint
used_configuration = api_configuration.ApiConfiguration(
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(used_configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example passing only required values which don't have defaults set
    query_params: operation.RequestQueryParameters.Params = {
        'username': "CbUUGjjNSwg0_bs9ZayIMrKdgNvb6gvxmPb9GcsM61ate1RA89q3w1l4eH4XxEz.5awLMdeXylwK0lMGUSM4jsrh4dstlnQUN5vVdMLPA",
        'password': "password_example",
    }
    try:
        # Logs user into the system
        api_response = api_instance.login_user(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->login_user: %s\n" % e)
```

[[Back to top]](#top)
[[Back to UserApi API]](../../apis/tags/user_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)