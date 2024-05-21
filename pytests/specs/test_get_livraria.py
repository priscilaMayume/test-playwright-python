from pytests.clients.common import Common
from pytests.clients.livraria_client import LivrariaClient
from pytests.schemas.get_id_livro_sucess_schema import *
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *
from pytests.exemples.exemples_test_get_livraria import *

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

@pytest.mark.crud_livros
@pytest.mark.parametrize("value, code", exemples_get_livraria_invalid_values)
def test_get_id_livro_invalid(value, code):
    client = LivrariaClient()
    client.set_base_url()
    values_change = Common.values_change(value)
    response = client.get_livros(values_change)
    Common.validate_response(response, code)