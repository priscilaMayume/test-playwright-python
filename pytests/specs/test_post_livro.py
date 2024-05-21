import pytest
import os
from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.livraria_client import LivrariaClient
from pytests.clients.common import Common
from pytests.support.api_utils import ApiUtils
from pytests.schemas.post_registrar_livro_com_sucesso_schema import *
from pytests.exemples.exemples_test_post_livraria import *
from pytests.clients.livraria_client import LivrariaClient

@pytest.mark.crud_livros
def test_post_registrar_livro_com_sucesso():
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    path = "livros"
    response = client.post_livros(path, payload)
    LivrariaClient.validate_response(response, 201)
    ApiUtils.validate_json_schema(response,post_schema)

@pytest.mark.crud_livros
@pytest.mark.parametrize("payload, code", exemples_post_livraria_invalid_payload)
def test_post_livros_invalid_payload(payload, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = Common.incorrect_payload(payload)
    ApiUtils.payload_parse(payload)
    path = "livros"
    response = client.post_livros(path, payload)
    LivrariaClient.validate_response(response, code)

@pytest.mark.crud_livros
@pytest.mark.parametrize("field, value, code", exemples_post_livraria_invalid_values)
def test_post_livros_invalid_values(field, value, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    payload = Common.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse(payload)
    path = "livros"
    response = client.post_livros(path, payload)
    LivrariaClient.validate_response(response, code)

@pytest.mark.crud_livros
@pytest.mark.parametrize("field, code", exemples_post_livraria_no_fields)
def test_post_livros_no_fields(field, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    payload = Common.remove_fields_payload(payload, field)
    ApiUtils.payload_parse(payload)
    path = "livros"
    response = client.post_livros(path, payload)
    LivrariaClient.validate_response(response, code)

