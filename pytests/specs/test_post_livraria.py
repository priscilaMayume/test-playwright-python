from pytests.clients.common import Common
from pytests.support.hooks import *
from pytests.clients.livraria_client import LivrariaClient
from pytests.exemples.exemples_test_post_livraria import *
from pytests.mocks.livraria_mock import *
from pytests.schemas.post_new_livro_sucess_schema import *
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *

@pytest.mark.crud_livros
def test_post_new_livro_sucess():
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = client.post_livros(payload)
    Common.validate_response(response, 201)
    ApiUtils.validate_json_schema(response, post_new_livro_sucess_schema)


@pytest.mark.crud_livros
@pytest.mark.parametrize("payload, code", exemples_post_livraria_invalid_payload)
def test_post_livros_invalid_payload(payload, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = Common.incorrect_payload(payload)
    ApiUtils.payload_parse(payload)
    response = client.post_livros(payload)
    Common.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("field, value, code", exemples_post_livraria_invalid_values)
def test_post_livros_invalid_values(field, value, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    payload = Common.change_fields_payload(payload, field, value)
    ApiUtils.payload_parse(payload)
    response = client.post_livros(payload)
    Common.validate_response(response, code)


@pytest.mark.crud_livros
@pytest.mark.parametrize("field, code", exemples_post_livraria_no_fields)
def test_post_livros_no_fields(field, code):
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    payload = Common.remove_fields_payload(payload, field)
    ApiUtils.payload_parse(payload)
    response = client.post_livros(payload)
    Common.validate_response(response, code)
