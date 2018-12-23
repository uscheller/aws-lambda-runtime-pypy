import unittest
from requests import Response
from runtime_interface import RuntimeInterface


class TestRuntimeInterface(RuntimeInterface):
    def __init__(self, api):
        super(TestRuntimeInterface, self).__init__(api)
        self.last_request_id = None
        self.last_response = None

    def fetch_next_request(self):
        response = Response()
        response.json = lambda: {}
        return "requestId", response

    def post_response(self, request_id, response):
        self.last_request_id = request_id
        self.last_response = response


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.runtime = TestRuntimeInterface("localhost:8080")

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


if __name__ == '__main__':
    unittest.main()
