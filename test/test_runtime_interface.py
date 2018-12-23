import os
import unittest
from unittest.mock import Mock
from runtime_interface import RuntimeInterface


class TestRuntimeInterface(RuntimeInterface):
    def __init__(self):
        super(TestRuntimeInterface, self).__init__()
        self.last_request_id = None
        self.last_response = None

    def fetch_next_request(self):
        response = Mock()
        response.json = lambda: {}
        return "requestId", response

    def post_response(self, request_id, response):
        self.last_request_id = request_id
        self.last_response = response


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        os.environ["AWS_LAMBDA_RUNTIME_API"] = "localhost:8080"
        os.environ["_HANDLER"] = "handler.hello"
        self.runtime = TestRuntimeInterface()

    def test_urls(self):
        self.assertEqual(self.runtime.fetch_url,
            "http://localhost:8080/2018-06-01/runtime/invocation/next")
        self.assertEqual(self.runtime.response_url,
            "http://localhost:8080/2018-06-01/runtime/invocation/{}/response")
        self.assertEqual(self.runtime.error_url,
            "http://localhost:8080/2018-06-01/runtime/invocation/{}/error")

    def test_process_event(self):
        self.runtime.process_event()
        self.assertEqual(self.runtime.last_request_id, "requestId")

    def test_process_event_different_handler(self):
        os.environ["_HANDLER"] = "handler.primes"
        self.runtime = TestRuntimeInterface()
        self.runtime.process_event()
        self.assertEqual(self.runtime.last_request_id, "requestId")


if __name__ == '__main__':
    unittest.main()
