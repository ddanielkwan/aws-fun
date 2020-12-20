import boto3
def get_s3_client():
    session = boto3.Session(aws_access_key_id="xxx", aws_secret_access_key= "xxx")
    return session.client('s3')
