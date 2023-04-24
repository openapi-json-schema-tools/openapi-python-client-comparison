openapi_client.paths.store_order_order_id.operation
# Operation Method Name

| Method Name | Api Class | Notes |
| ----------- | --------- | ----- |
| delete_order | [StoreApi](../../apis/tags/store_api.md) | This api is only for tag=store |
| delete | ApiForDelete | This api is only for this endpoint |
| delete | StoreOrderOrderId | This api is only for path=/store/order/{orderId} |

## Table of Contents
- [General Info](#general-info)
- [Arguments](#arguments)
- [Return Types](#return-types)
- [Servers](#servers)
- [Code Sample](#code-sample)

## General Info
| Field | Value |
| ----- | ----- |
| Summary | Delete purchase order by ID |
| Description | For valid response try integer IDs with value < 1000. Anything above 1000 or nonintegers will generate API errors |
| Path | "/store/order/{orderId}" |
| HTTP Method | delete |

## Arguments

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
[path_params](#path_params) | [RequestPathParameters.Params](#requestpathparametersparams), dict | |
server_index | typing.Optional[int] | default is None | Allows one to select a different server
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParameters.Params
This is a TypedDict

Key | Input Type | Description  | Notes
------------- | ------------- | ------------- | -------------
orderId | [Parameter0.schema](#parameter0-schema), str | | 


#### Parameter0

##### Description
ID of the order that needs to be deleted

##### Parameter0 Schema

###### Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str | str |  |

## Return Types

HTTP Status Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
400 | [ResponseFor400.response_cls](#responsefor400-response_cls) | Invalid ID supplied
404 | [ResponseFor404.response_cls](#responsefor404-response_cls) | Order not found

## ResponseFor400

### Description
Invalid ID supplied

### ResponseFor400 response_cls
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

## ResponseFor404

### Description
Order not found

### ResponseFor404 response_cls
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
from openapi_client.apis.tags import store_api
from openapi_client.paths.store_order_order_id.delete import operation
from pprint import pprint
used_configuration = api_configuration.ApiConfiguration(
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(used_configuration) as api_client:
    # Create an instance of the API class
    api_instance = store_api.StoreApi(api_client)

    # example passing only required values which don't have defaults set
    path_params: operation.RequestPathParameters.Params = {
        'orderId': "orderId_example",
    }
    try:
        # Delete purchase order by ID
        api_response = api_instance.delete_order(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StoreApi->delete_order: %s\n" % e)
```

[[Back to top]](#top)
[[Back to StoreApi API]](../../apis/tags/store_api.md)
[[Back to Endpoints]](../../../README.md#Endpoints) [[Back to README]](../../../README.md)