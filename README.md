# openapi-python-client-comparison
openapi python client comparison

A repo to compare openapi python clients

## Implementations Included
- [swagger-codegen](https://github.com/swagger-api/swagger-codegen), python generator
- [openapi-generator](https://github.com/OpenAPITools/openapi-generator)
  - python-prior generator
  - python-nextgen
- [openapi-json-schema-generator](https://github.com/openapi-json-schema-tools/openapi-json-schema-generator), python generator

## Openapi Documents and Purposes

| Document | Purpose | Provenance |
| -------- | ------- | ---------- |
| petstore.yaml | standard api | [openapi-generator repo](https://github.com/OpenAPITools/openapi-generator/blob/917892db7d1dc5a459bdf6d499a491367fc97751/modules/openapi-generator/src/test/resources/3_0/petstore.yaml)

## Generated Code Amount
via vscode code counter tool

### petstore.yaml

| Generator | Files | Code |
| -------- | ----- | ---- |
| openapi_generator_python_nextgen | 27 | 2712 |
| openapi_generator_python_prior | 30 | 5075 |
| openapi_json_schema_generator_python | 365 | 12701


### openapi_json_schema_generator_python breakdown
- 7.8k src/openapi_client/paths
- most of this comes from the 3x operation typing overloads

Reasons for the openapi json scheme generator difference
- has overload type hints on all endpoints, allows input content type selection
- json paths used to create files so many files made
- object models have `__getitem__` methods for properties
- most of the code comes from paths, can itbe reduced?

## Generate

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli:2.4.31 generate \
    -i /local/petstore.yaml \
    -l python \
    -o /local/swagger_codegen_python

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v6.5.0 generate \
    -i /local/petstore.yaml \
    -g python-prior \
    -o /local/openapi_generator_python_prior

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v6.5.0 generate \
    -i /local/petstore.yaml \
    -g python-nextgen \
    -o /local/openapi_generator_python_nextgen

docker run --rm -v "${PWD}:/local" openapijsonschematools/openapi-json-schema-generator-cli:3.0.0-latest generate \
    -i /local/petstore.yaml \
    -g python \
    -o /local/openapi_json_schema_generator_python