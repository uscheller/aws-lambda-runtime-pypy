import unittest
from runtime_interface import RuntimeInterface


class TestStringMethods(unittest.TestCase):

    def test_urls(self):
        runtime = RuntimeInterface("localhost:8080")
        self.assertEqual(runtime.fetch_url,
            "http://localhost:8080/2018-06-01/runtime/invocation/next")
        self.assertEqual(runtime.response_url,
            "http://localhost:8080/2018-06-01/runtime/invocation/{}/response")
        self.assertEqual(runtime.error_url,
            "http://localhost:8080/2018-06-01/runtime/invocation/{}/error")

if __name__ == '__main__':
    unittest.main()
