# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from openapi_client.components.schema.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from openapi_client.components.schema.api_response import ApiResponse
from openapi_client.components.schema.category import Category
from openapi_client.components.schema.order import Order
from openapi_client.components.schema.pet import Pet
from openapi_client.components.schema.tag import Tag
from openapi_client.components.schema.user import User
