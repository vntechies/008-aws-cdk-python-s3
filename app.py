#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_python_s3.aws_cdk_python_s3_stack import AwsCdkPythonS3Stack


app = cdk.App()
AwsCdkPythonS3Stack(app, "aws-cdk-python-s3")

app.synth()
