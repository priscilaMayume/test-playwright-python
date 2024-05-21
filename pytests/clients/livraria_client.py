import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import LOG

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

class LivrariaClient:
    def __init__(self):
        self.base_url = None

    def set_base_url(self):
        self.base_url = os.environ['BASE_URL']

    def post_livros(self, path, payload):
        if self.base_url is None:
            raise ValueError("A URL base não foi definida. Use set_base_url() para definir a URL base antes de fazer a requisição.")

        url = f"{self.base_url}{path}"
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.post(url, data=payload, headers={"Content-Type": "application/json"})
            LOG.log_info("POST")
            LOG.log_info(url)
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    def get_livros(self, path):
        if self.base_url is None:
            raise ValueError("A URL base não foi definida. Use set_base_url() para definir a URL base antes de fazer a requisição.")

        url = f"{self.base_url}{path}"
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.get(url)
            LOG.log_info("GET")
            LOG.log_info(url)
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    @staticmethod
    def validate_response(response, code):
        ApiUtils.request_parse_log(response)
        ApiUtils.validate_status_code(response, code)
