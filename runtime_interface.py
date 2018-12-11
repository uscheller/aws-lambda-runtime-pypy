"""
A Custom Runtime Interface for running Python code with Pypy on AWS Lambda
"""
import sys
import json
import requests
import handler

__author__ = "Ulrich Scheller"
__email__ = "mail@ulrich-scheller.de"
__website__ = "www.ulrich-scheller.de"
__status__ = "Prototype"


class RuntimeInterface(object):
    def __init__(self, AWS_LAMBDA_RUNTIME_API):
        path = "2018-06-01/runtime/invocation"
        self.fetch_url = "http://{}/{}/next".format(AWS_LAMBDA_RUNTIME_API, path)
        self.response_url = "http://{}/{}/{}/response".format(AWS_LAMBDA_RUNTIME_API, path, "{}")

    def fetch_next_request(self):
        response = requests.get(self.fetch_url)
        return response.headers["Lambda-Runtime-Aws-Request-Id"], response

    def post_response(self, request_id, response):
        url = self.response_url.format(request_id)
        requests.post(url, data=json.dumps(response))

    def process_event(self):
        request_id, r = self.fetch_next_request()
        response = handler.hello(r.json(), None)
        self.post_response(request_id, response)

    def run_loop(self):
        while True:
            self.process_event()


if __name__ == "__main__":
    AWS_LAMBDA_RUNTIME_API = sys.argv[1]
    runtime = RuntimeInterface(AWS_LAMBDA_RUNTIME_API)
    runtime.run_loop()
