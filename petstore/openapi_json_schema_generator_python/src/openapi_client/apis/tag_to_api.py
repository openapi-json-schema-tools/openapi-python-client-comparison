import typing
import typing_extensions

from openapi_client.apis.tags.pet_api import PetApi
from openapi_client.apis.tags.store_api import StoreApi
from openapi_client.apis.tags.user_api import UserApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        "pet": typing.Type[PetApi],
        "store": typing.Type[StoreApi],
        "user": typing.Type[UserApi],
    }
)

tag_to_api = TagToApi(
    {
        "pet": PetApi,
        "store": StoreApi,
        "user": UserApi,
    }
)
