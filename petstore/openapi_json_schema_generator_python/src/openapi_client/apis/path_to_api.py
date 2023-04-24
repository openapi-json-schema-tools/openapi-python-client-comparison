import typing
import typing_extensions

from openapi_client.apis.paths.pet import Pet
from openapi_client.apis.paths.pet_find_by_status import PetFindByStatus
from openapi_client.apis.paths.pet_find_by_tags import PetFindByTags
from openapi_client.apis.paths.pet_pet_id import PetPetId
from openapi_client.apis.paths.pet_pet_id_upload_image import PetPetIdUploadImage
from openapi_client.apis.paths.store_inventory import StoreInventory
from openapi_client.apis.paths.store_order import StoreOrder
from openapi_client.apis.paths.store_order_order_id import StoreOrderOrderId
from openapi_client.apis.paths.user import User
from openapi_client.apis.paths.user_create_with_array import UserCreateWithArray
from openapi_client.apis.paths.user_create_with_list import UserCreateWithList
from openapi_client.apis.paths.user_login import UserLogin
from openapi_client.apis.paths.user_logout import UserLogout
from openapi_client.apis.paths.user_username import UserUsername

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
    "/pet": typing.Type[Pet],
    "/pet/findByStatus": typing.Type[PetFindByStatus],
    "/pet/findByTags": typing.Type[PetFindByTags],
    "/pet/{petId}": typing.Type[PetPetId],
    "/pet/{petId}/uploadImage": typing.Type[PetPetIdUploadImage],
    "/store/inventory": typing.Type[StoreInventory],
    "/store/order": typing.Type[StoreOrder],
    "/store/order/{orderId}": typing.Type[StoreOrderOrderId],
    "/user": typing.Type[User],
    "/user/createWithArray": typing.Type[UserCreateWithArray],
    "/user/createWithList": typing.Type[UserCreateWithList],
    "/user/login": typing.Type[UserLogin],
    "/user/logout": typing.Type[UserLogout],
    "/user/{username}": typing.Type[UserUsername],
    }
)

path_to_api = PathToApi(
    {
    "/pet": Pet,
    "/pet/findByStatus": PetFindByStatus,
    "/pet/findByTags": PetFindByTags,
    "/pet/{petId}": PetPetId,
    "/pet/{petId}/uploadImage": PetPetIdUploadImage,
    "/store/inventory": StoreInventory,
    "/store/order": StoreOrder,
    "/store/order/{orderId}": StoreOrderOrderId,
    "/user": User,
    "/user/createWithArray": UserCreateWithArray,
    "/user/createWithList": UserCreateWithList,
    "/user/login": UserLogin,
    "/user/logout": UserLogout,
    "/user/{username}": UserUsername,
    }
)
