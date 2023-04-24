openapi_client.components.schema.user
# Schema User

## Description
A User who is purchasing from the pet store

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict | A User who is purchasing from the pet store |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int | decimal.Decimal |  | [optional] value must be a 64 bit integer
**username** | str | str |  | [optional]
**firstName** | str | str |  | [optional]
**lastName** | str | str |  | [optional]
**email** | str | str |  | [optional]
**password** | str | str |  | [optional]
**phone** | str | str |  | [optional]
**userStatus** | decimal.Decimal, int | decimal.Decimal | User Status | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema | frozendict.frozendict, tuple, decimal.Decimal, str, bytes, BoolClass, NoneClass, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
