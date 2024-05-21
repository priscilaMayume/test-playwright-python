import os

import self
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from pytests.support.hooks import LOG

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


class LivrariaClient:
    def __init__(self):
        self.base_url = None

    def set_base_url(self):
        self.base_url = os.environ['BASE_URL']

    def post_livros(self, payload):
        if self.base_url is None:
            raise ValueError(
                "A URL base não foi definida. Use set_base_url() para definir a URL base antes de fazer a requisição.")

        url = f"{self.base_url}"
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.post(url, data=payload, headers={"Content-Type": "application/json"})
            LOG.log_info("POST")
            LOG.log_info(url)
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    def get_livros(self, id=""):
        if self.base_url is None:
            raise ValueError(
                "A URL base não foi definida. Use set_base_url() para definir a URL base antes de fazer a requisição.")

        url = f"{self.base_url}{id}"
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.get(url)
            LOG.log_info("GET")
            LOG.log_info(url)
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    def put_livros(self, payload, id):
        if self.base_url is None:
            raise ValueError(
                "A URL base não foi definida. Use set_base_url() para definir a URL base antes de fazer a requisição."
            )

        url = f"{self.base_url}{id}"
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.put(url, data=payload, headers={"Content-Type": "application/json"})
            LOG.log_info("PUT")
            LOG.log_info(url)
            return {"code": response.status, "body": response.text(), "headers": response.headers}

    def patch_livros(self, payload, id):
        if self.base_url is None:
            raise ValueError(
                "A URL base não foi definida. Use set_base_url() para definir a URL base antes de fazer a requisição."
            )

        url = f"{self.base_url}{id}"
        with sync_playwright() as p:
            context = p.request.new_context()
            response = context.patch(url, data=payload, headers={"Content-Type": "application/json"})
            LOG.log_info("PATCH")
            LOG.log_info(url)
            return {"code": response.status, "body": response.text(), "headers": response.headers}
