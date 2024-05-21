from pytests.clients.common import Common
from pytests.clients.livraria_client import LivrariaClient
from pytests.mocks.livraria_mock import *
from pytests.schemas.patch_livro_sucess_schema import *
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *


@pytest.mark.crud_livros
def test_patch_livro_sucess():
    client = LivrariaClient()
    client.set_base_url()
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    response = client.patch_livros(payload, 3)
    Common.validate_response(response, 200)
    ApiUtils.validate_json_schema(response, patch_livro_sucess_schema)