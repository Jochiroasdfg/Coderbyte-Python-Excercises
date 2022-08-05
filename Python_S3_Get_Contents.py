import boto3
from botocore.handlers import disable_signing
resource = boto3.resource('s3')
resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)

bucket = resource.Bucket('coderbytechallengesandbox')

for item in bucket.objects.all():
    if "__cb__" in item.key:
        contents = item.get()["Body"].read().decode("utf-8")
        print(contents)