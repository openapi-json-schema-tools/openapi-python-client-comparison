# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.paths.pet_find_by_status.get.operation import FindPetsByStatus
from openapi_client.paths.pet_find_by_tags.get.operation import FindPetsByTags
from openapi_client.paths.pet_pet_id_upload_image.post.operation import UploadFile
from openapi_client.paths.pet_pet_id.delete.operation import DeletePet
from openapi_client.paths.pet_pet_id.get.operation import GetPetById
from openapi_client.paths.pet_pet_id.post.operation import UpdatePetWithForm
from openapi_client.paths.pet.post.operation import AddPet
from openapi_client.paths.pet.put.operation import UpdatePet


class PetApi(
    FindPetsByStatus,
    FindPetsByTags,
    UploadFile,
    DeletePet,
    GetPetById,
    UpdatePetWithForm,
    AddPet,
    UpdatePet,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    pass
