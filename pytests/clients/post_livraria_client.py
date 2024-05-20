from playwright.sync_api import sync_playwright
from pytests.support.api_utils import ApiUtils
from pytests.support.hooks import *
import os

class PostLivrariaClient:

    @staticmethod
    def post_livros(uri, payload):
        with sync_playwright() as p:
            context = p.request.new_context()
            #caso tivesse headrs, token, etc -> response = context.post("url", data=payload, token =, headers=, )
            response = context.post(uri, data=payload)
            LOG.log_info("POST")
            LOG.log_info(uri)
            return {"code": response.status, "body": response.text(), "headers": response.headers}


    @staticmethod
    def validate_response(response, code):
        ApiUtils.request_parse_log(response)
        ApiUtils.validate_status_code(response, code)
