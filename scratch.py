import jsonschema

req1 = {
    "executionId": "12345678-1234-1234-1234-123456789012",
    "modelName": "ptxmodel_ie",
    "modelVersion": 1,
    "inputData": {"fileName": "input/03.0000002a.png"},
}
png_req = {
    "executionId": "12345678-1234-1234-1234-123456789012",
    "modelName": "ptxmodel_ie",
    "modelVersion": 1,
    "inputData": {"fileName": "input/03.0000002a.png"},
}

req = {
    "executionId": "12345678-1234-1234-1234-123456789012",
    "modelName": "ptxmodel_ie",
    "modelVersion": 1,
    "inputData": {"binaryFileName": "input/03.0000002a.bin",
                  "shape":[1,2]},
}

idata =  {"binaryFileName": "input/03.0000002a.bin1",
                  "shape":[1,2]}

DEFAULT_EXECUTION_REQUEST_SCHEMA = {
    "id": "ac310688-f748-11e8-8eb2-f2801f1b9fd1",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "definitions": {
        "fileName": {
            "type": "object",
            "$comment": "fileName is required.",
            "properties": {
                "fileName": {
                    "type": "string",
                    "pattern": "[a-zA-Z0-9-].(jpg|jpeg|png|dcm)$",
                }
            },
            "required": ["fileName"],
        },
        "binaryFileName": {
            "type": "object",
            "$comment": "Binary data is required.",
            "properties": {"binaryFileName": {"type": "string",
                                              "pattern": "[a-zA-Z0-9-].bin$"},
                           "shape": {
                               "type": "array",
                                "minItems": 2,
                                "maxItems": 2
                           }},
            "required": ["binaryFileName","shape"],
        },
        "binaryData": {
            "type": "object",
            "$comment": "Binary data is required.",
            "properties": {"binaryData": {"type": "string"},
                           "shape": {
                               "type": "array",
                                "minItems": 2,
                                "maxItems": 2
                           }
                           },
            "required": ["binaryData","shape"],
        },
    },
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "executionId": {
            "$comment": "Unique identifier (an alpha-numeric pattern of 8-4-4-4-12) of the execution request being dispatched",
            "type": "string",
            "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
        },
        "modelName": {
            "$comment": "Model Name required for inferencing that must be a string and between the length of 1-255 characters",
            "type": "string",
            "minLength": 1,
            "maxLength": 255,
        },
        "modelVersion": {
            "$comment": "Version used for inference when multiple model versions are deployed. Defaults to latest when not provided",
            "type": "integer",
        },
        "inputData": {
            "type": "object",
            "$comment": "Input data to be used for completing the inference",
            "oneOf": [
                {"$ref": "#/definitions/fileName"},
                {"$ref": "#/definitions/binaryFileName"},
                {"$ref": "#/definitions/binaryData"},
            ],
        },
    },
    "required": ["executionId", "modelName", "inputData"],
}

PTX_SCHEMA = {
    "id": "ac310688-f748-11e8-8eb2-f2801f1b9fd1",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "fileName": {
                    "type": "string",
                    "pattern": "[a-zA-Z0-9-].(jpg|jpeg|png|dcm)$",
                },
"binaryFileName": {"type": "string",
                                              "pattern": "[a-zA-Z0-9-].bin$"},
                           "binaryData": {"type": "string"},
                           "shape": {
                               "type": "array",
                               "minItems": 2,
                               "maxItems": 2
                           }
    },
    "oneOf": [
        {"required": ["fileName"]},
        {"required": ["binaryFileName","shape"]},
        {"required": ["binaryData","shape"]}
    ]
}


# {
#     "id": "ac310688-f748-11e8-8eb2-f2801f1b9fd1",
#     "$schema": "http://json-schema.org/draft-04/schema#",
#     "type": "object",
#     "additionalProperties": False,
#     "properties": {
#         "executionId": {
#             "$comment": "Unique identifier (an alpha-numeric pattern of 8-4-4-4-12) of the execution request being dispatched",
#             "type": "string",
#             "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"
#         },
#         "modelName": {
#             "$comment": "Model Name required for inferencing that must be a string and between the length of 1-255 characters",
#             "type": "string",
#             "minLength": 1,
#             "maxLength": 255
#         },
#         "modelVersion": {
#             "$comment": "Version used for inference when multiple model versions are deployed. Defaults to latest when not provided",
#             "type": "integer"
#         },
#         "inputData": {
#             "$comment": "Input data to be used for completing the inference",
#             "type": "object"
#         }
#     },
#     "required": ["executionId", "modelName", "inputData"]
# }
try:
    #jsonschema.validate(png_req, schema=DEFAULT_EXECUTION_REQUEST_SCHEMA)
    jsonschema.validate(idata,schema=PTX_SCHEMA)
except Exception as e:
    print ("Exceptipon ___________")
    print(e)
    print(str(e))
