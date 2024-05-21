from pytests.clients.common import Common
from pytests.clients.livraria_client import LivrariaClient
from pytests.mocks.livraria_mock import *
from pytests.schemas.patch_livro_sucess_schema import *
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *
from pytests.exemples.exemplos_test_patch_livraria import *


@pytest.mark.crud_livros
def test_patch_livro_sucess():
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = client.patch_livros(payload, 3)
    Common.validate_response(response, 200)
    ApiUtils.validate_json_schema(response, patch_livro_sucess_schema)

@pytest.mark.crud_livros
@pytest.mark.parametrize("payload, code", exemples_patch_livraria_invalid_payload)
def test_patch_livros_invalid_payload(payload, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = Common.incorrect_payload(payload)
    ApiUtils.payload_parse(payload)
    response = client.patch_livros(payload, 3)
    Common.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("field, value, code", exemples_patch_livraria_invalid_values)
def test_patch_livros_invalid_values(field, value, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    payload = Common.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse(payload)
    response = client.patch_livros(payload, 3)
    Common.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("field, code", exemples_patch_livraria_no_fields)
def test_patch_livros_no_fields(field, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    payload = Common.remove_fields_payload(payload, field)
    ApiUtils.payload_parse(payload)
    response = client.patch_livros(payload, 3)
    Common.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("value, code", exemples_patch_id_livraria_invalid_values)
def test_patch_id_livro_invalid(value, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    values_change = Common.values_change(value)
    response = client.patch_livros(payload, values_change)
    Common.validate_response(response, code)
