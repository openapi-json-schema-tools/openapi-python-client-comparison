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

| Language | Files | % | Code | % | Comment | % |
| -------- | ----- | - | ---- | - | ------- | - |
| openapi_generator_python_prior | 45 | 100.0 | 4637 |  42.7 |    3371 | 31.1 |


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

docker run --rm -v "${PWD}:/local" openapjsonschematools/openapi-json-schema-generator-cli:2.0.0 generate \
    -i /local/petstore.yaml \
    -g python \
    -o /local/openapi_json_schema_generator_python