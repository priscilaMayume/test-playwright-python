import pytests
from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.post_livraria_client import PostLivrariaClient
from pytests.support.api_utils import ApiUtils
from pytests.schemas.post_registrar_livro_com_sucesso_schema import *
import os

def test_post_registrar_livro_com_sucesso():
    payload = payload_post_livros()
    ApiUtils.payload_parse(payload)
    uri = f"{os.environ['BASE_URL']}livros"
    response = PostLivrariaClient.post_livros(uri, payload)
    PostLivrariaClient.validate_response(response, 201)
    ApiUtils.validate_json_schema(response, post_shema)
