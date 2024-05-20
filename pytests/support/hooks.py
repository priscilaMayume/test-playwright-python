import pytest
from pytests.support.log_service import LogService
from dotenv import load_dotenv

LOG = LogService()

#Ele executa uma unica vez dentro da sessão
@pytest.fixture(scope="session", autouse=True)
def before_all():
    LOG.log_info("Teste log before all")
    load_dotenv()

# Executar antes de cada teste
@pytest.fixture(autouse=True)
def before_after():
    LOG.log_info("Teste log before")
    yield
    LOG.log_info("Teste log after")