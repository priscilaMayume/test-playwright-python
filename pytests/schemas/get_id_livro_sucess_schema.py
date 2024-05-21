get_id_livro_sucess_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "array",
    "items": [
        {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer"
                },
                "nome": {
                    "type": "string"
                },
                "autor": {
                    "type": "string"
                },
                "data_publicacao": {
                    "type": "string"
                },
                "qtde_paginas": {
                    "type": "integer"
                },
                "created_on": {
                    "type": "string"
                },
                "update_at": {
                    "type": "null"
                }
            },
            "required": [
                "id",
                "nome",
                "autor",
                "data_publicacao",
                "qtde_paginas",
                "created_on",
                "update_at"
            ]
        }
    ]
}