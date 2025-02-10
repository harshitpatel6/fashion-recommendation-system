import boto3
from config import AWS_S3_BUCKET

s3 = boto3.client("s3")

def upload_image_to_s3(file_path, key):
    s3.upload_file(file_path, AWS_S3_BUCKET, key)
    return f"https://{AWS_S3_BUCKET}.s3.amazonaws.com/{key}"
