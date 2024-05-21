from pytests.clients.common import Common
from pytests.clients.livraria_client import LivrariaClient
from pytests.exemples.exemples_teste_put_livraria import *
from pytests.mocks.livraria_mock import *
from pytests.schemas.put_livro_sucess_schema import *
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *


@pytest.mark.crud_livros
def test_put_livro_sucess():
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = client.put_livros(payload, 4)
    Common.validate_response(response, 200)
    ApiUtils.validate_json_schema(response, put_livro_sucess_schema)


@pytest.mark.crud_livros
@pytest.mark.parametrize("payload, code", exemples_put_livraria_invalid_payload)
def test_put_livros_invalid_payload(payload, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = Common.incorrect_payload(payload)
    ApiUtils.payload_parse(payload)
    response = client.put_livros(payload, 4)
    Common.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("field, value, code", exemples_put_livraria_invalid_values)
def test_put_livros_invalid_values(field, value, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    payload = Common.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse(payload)
    response = client.put_livros(payload, 4)
    Common.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("field, code", exemples_put_livraria_no_fields)
def test_put_livros_no_fields(field, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    payload = Common.remove_fields_payload(payload, field)
    ApiUtils.payload_parse(payload)
    response = client.put_livros(payload, 4)
    Common.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("value, code", exemples_put_id_livraria_invalid_values)
def test_put_id_livro_invalid(value, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    values_change = Common.values_change(value)
    response = client.put_livros(payload, values_change)
    Common.validate_response(response, code)
