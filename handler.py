import json
import math

def hello(event, context):
    primes = [x for x in range(2, 200000) if [y for y in range(2, int(math.sqrt(x))) if x%y == 0] == []]
    body = {
        "message": "Hello from {}! Your function executed successfully!" +
        "\nnumber of primes: {}".format(sys.argv[0].split("/")[-1], str(len(primes))),
        #"input": event,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
