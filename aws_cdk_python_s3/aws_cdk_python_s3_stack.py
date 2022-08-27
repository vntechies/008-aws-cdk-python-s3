from constructs import Construct
from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_s3 as s3,
    aws_kms as kms,
)


class AwsCdkPythonS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, "VNTechies-AWS-CDK-S3-demo-bucket",
                           object_ownership=s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
                           block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                           encryption_key=kms.Key(self, 'VNTechies-AWS-CDK-S3-demo-bucket-key'),)

        bucket.grant_read(iam.AccountRootPrincipal())
