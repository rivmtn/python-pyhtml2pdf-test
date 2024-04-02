import boto3

from v1.config import S3_REGION_NAME, S3_ACCESS_KEY, S3_SECRET_KEY

s3 = boto3.client(
    service_name='s3',
    region_name=S3_REGION_NAME,
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
)
