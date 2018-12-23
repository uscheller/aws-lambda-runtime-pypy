# aws-lambda-runtime-pypy
Custom Runtime for AWS Lambda using the Pypy interpreter. This was inspired by
the [AWS Tutorial for creating a Custom Runtime](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-walkthrough.html)

This runtime is experimental and a Proof of Concept.

## Details

 * Uses a plain Pypy distribution downloaded from https://pypy.org/download.html
 * Deployed package is around 30 MB in size
 * Long running tasks benefit from using Pypy on Lambda
 * Short running, not CPU limited tasks are better of using the default Python runtime
 
## Usage

You should have your AWS tools and credentials set up and the [Serverless Framework](https://serverless.com/) installed.

Run
```bash
sls deploy
```
for deploying this example Lambda based on a Pypy runtime to AWS.

## Credits

Created by Ulrich Scheller

More details can be found in [this blog post](https://www.ulrich-scheller.de/a-pypy-runtime-for-aws-lambda/)
