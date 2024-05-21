from pytests.clients.common import Common
from pytests.clients.livraria_client import LivrariaClient
from pytests.mocks.livraria_mock import payload_post_livros
from pytests.schemas.delete_id_livro_sucess_schema import *
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *
from pytests.exemples.exemples_test_delete_livraria import *
import json


@pytest.mark.crud_livros
def test_delete_id_livro_sucess():
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = client.post_livros(payload)
    Common.validate_response(response, 201)

    response_json = json.loads(response['body'])
    id = response_json['id']
    response = client.delete_livros(id)
    ApiUtils.validate_json_schema(response, delete_livro_sucess_schema)
    Common.validate_response(response, 200)


@pytest.mark.crud_livros
@pytest.mark.parametrize("value, code", exemples_delete_livraria_invalid_values)
def test_delete_id_livro_invalid(value, code):
    client = LivrariaClient()
    client.set_base_url()
    values_change = Common.values_change(value)
    response = client.delete_livros(values_change)
    Common.validate_response(response, code)
