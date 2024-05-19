import pytests
from pytests.support.hooks import *
from pytests.mocks.livraria_mock import *
from pytests.clients.post_livraria_client import PostLivrariaClient

def test_post_livro():
    payload = payload_post_livros()
    PostLivrariaClient.post_livros(payload)
