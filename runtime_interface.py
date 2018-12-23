"""
A Custom Runtime Interface for running Python code with Pypy on AWS Lambda
"""
import os
import json
import requests
import importlib

__author__ = "Ulrich Scheller"
__email__ = "mail@ulrich-scheller.de"
__website__ = "www.ulrich-scheller.de"
__status__ = "Prototype"


class RuntimeInterface(object):
    def __init__(self):
        api = os.getenv("AWS_LAMBDA_RUNTIME_API")
        handler = os.getenv("_HANDLER")
        handler_name, handler_method_name = handler.split(".")
        handler = importlib.import_module(handler_name)
        self.handler_method = getattr(handler, handler_method_name)
        url_scheme = "http://{}/2018-06-01/runtime/invocation".format(api)
        self.fetch_url = url_scheme + "/next"
        self.response_url = url_scheme + "/{}/response"
        self.error_url = url_scheme + "/{}/error"

    def fetch_next_request(self):
        response = requests.get(self.fetch_url)
        return response.headers["Lambda-Runtime-Aws-Request-Id"], response

    def post_response(self, request_id, response):
        url = self.response_url.format(request_id)
        requests.post(url, data=json.dumps(response))

    def post_error(self, request_id, error):
        url = self.error_url.format(request_id)
        print(error)
        error_response = {
            "errorMessage" : error.message,
            "errorType" : type(error)
        }
        requests.post(url, data=json.dumps(error_response))

    def process_event(self):
        request_id, r = self.fetch_next_request()
        try:
            response = self.handler_method(r.json(), None)
            self.post_response(request_id, response)
        except Exception as e:
            self.post_error(request_id, e)

    def run_loop(self):
        while True:
            self.process_event()


if __name__ == "__main__":
    runtime = RuntimeInterface()
    runtime.run_loop()
