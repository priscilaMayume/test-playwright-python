from pytests.clients.common import Common
from pytests.clients.livraria_client import LivrariaClient
from pytests.schemas.get_id_livro_sucess import *
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *


@pytest.mark.crud_livros
def test_get_all_livro_sucess():
    client = LivrariaClient()
    client.set_base_url()
    response = client.get_livros()
    Common.validate_response(response, 200)


@pytest.mark.crud_livros
def test_get_id_livro_sucess():
    client = LivrariaClient()
    client.set_base_url()
    idLivro = "3"
    response = client.get_livros(idLivro)
    Common.validate_response(response, 200)
    ApiUtils.validate_json_schema(response, get_id_livro_sucess_schema)
