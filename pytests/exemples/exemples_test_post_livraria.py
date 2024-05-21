exemples_post_livraria_invalid_payload = [
    ("payload_vazio", 400),
    ("None", 400),
    ("null", 400),
    ("hash_vazio", 400),
    ("array_vazio", 400),
    ("array_vazio_string", 400),
    ("payload_numb", 400),
    ("payload_boolean_true", 400),
    ("payload_boolean_false", 400)

]

exemples_post_livraria_invalid_values = [
    ("nome", "123", 400),
    #transformar em inteiro
    ("nome", "123_to_i", 400),
    #transformar em float
    ("nome", "123_to_f", 400),
    ("nome", "None", 400),
    ("nome", "Null", 400),
    ("nome", "number_negative", 400),
    ("nome", "boolean_true", 400),
    ("nome", "boolean_false", 400),
    ("nome", "256.characters_type_numbers", 400),
    ("nome", "256.characters_type_numbers", 400),
    ("nome", "Array", 400),
    ("nome", "Hash", 400),

    ("autor", "123", 400),
    ("autor", "123_to_i", 400),
    ("autor", "123_to_f", 400),
    ("autor", "None", 400),
    ("autor", "Null", 400),
    ("autor", "number_negative", 400),
    ("autor", "boolean_true", 400),
    ("autor", "boolean_false", 400),
    ("autor", "256.characters_type_numbers", 400),
    ("autor", "256.characters_type_numbers", 400),
    ("autor", "Array", 400),
    ("autor", "Hash", 400),

    ("dataPublicacao", "123", 400),
    ("dataPublicacao", "123_to_i", 400),
    ("dataPublicacao", "123_to_f", 400),
    ("dataPublicacao", "None", 400),
    ("dataPublicacao", "Null", 400),
    ("dataPublicacao", "number_negative", 400),
    ("dataPublicacao", "boolean_true", 400),
    ("dataPublicacao", "boolean_false", 400),
    ("dataPublicacao", "256.characters_type_numbers", 400),
    ("dataPublicacao", "256.characters_type_numbers", 400),
    ("dataPublicacao", "Array", 400),
    ("dataPublicacao", "Hash", 400),
    ("dataPublicacao", "12-06-2056", 400),
    ("dataPublicacao", "12/06/2056", 400),
    ("dataPublicacao", "2056/03/01", 400),

    ("qtdePaginas", "123", 400),
    ("qtdePaginas", "123_to_i", 400),
    ("qtdePaginas", "123_to_f", 400),
    ("qtdePaginas", "None", 400),
    ("qtdePaginas", "Null", 400),
    ("qtdePaginas", "number_negative", 400),
    ("qtdePaginas", "boolean_true", 400),
    ("qtdePaginas", "boolean_false", 400),
    ("qtdePaginas", "256.characters_type_numbers", 400),
    ("qtdePaginas", "256.characters_type_numbers", 400),
    ("qtdePaginas", "Array", 400),
    ("qtdePaginas", "Hash", 400)
]

exemples_post_livraria_no_fields = [
    ("nome", 400),
    ("autor", 400),
    ("dataPublicacao", 400),
    ("qtdePaginas", 400)
]


