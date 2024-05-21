from pytests.clients.common import Common
from pytests.clients.livraria_client import LivrariaClient
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
