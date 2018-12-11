# test
#from botocore.vendored import requests
import sys
import json
import requests
import handler


def process_event(AWS_LAMBDA_RUNTIME_API):
    global requestCount
    requestCount += 1
    r = requests.get("http://{}/2018-06-01/runtime/invocation/next".format(AWS_LAMBDA_RUNTIME_API))
    request_id = r.headers["Lambda-Runtime-Aws-Request-Id"]
    response = handler.hello(r.json(), None)
    body = json.loads(response["body"])
    body["debug"] = "requestCount: {}".format(requestCount)
    response["body"] = json.dumps(body)
    requests.post("http://{}/2018-06-01/runtime/invocation/{}/response".format(AWS_LAMBDA_RUNTIME_API, request_id), data=json.dumps(response))


if __name__ == "__main__":
    AWS_LAMBDA_RUNTIME_API = sys.argv[1]
    requestCount = 0
    while True:
        process_event(AWS_LAMBDA_RUNTIME_API)
