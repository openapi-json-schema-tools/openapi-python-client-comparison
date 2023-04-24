openapi_client.components.schema.pet
# Schema Pet

## Description
A pet for sale in the pet store

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict | A pet for sale in the pet store |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str | str |  |
**photoUrls** | list, tuple | [properties.PhotoUrls](#properties-photourls) |  |
**id** | decimal.Decimal, int | decimal.Decimal |  | [optional] value must be a 64 bit integer
**category** | [**Category**](category.md), dict, frozendict.frozendict | [**Category**](category.md) |  | [optional]
**tags** | list, tuple | [properties.Tags](#properties-tags) |  | [optional]
**status** | str | str | pet status in the store | [optional] must be one of ["available", "pending", "sold"]
**any_string_name** | dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema | frozendict.frozendict, tuple, decimal.Decimal, str, bytes, BoolClass, NoneClass, FileIO | any string name can be used but the value must be the correct type | [optional]

# properties PhotoUrls

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple | tuple |  |

## List Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str | str |  |

# properties Tags

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple | tuple |  |

## List Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Tag**](tag.md) | [**Tag**](tag.md) | [**Tag**](tag.md) |  |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
