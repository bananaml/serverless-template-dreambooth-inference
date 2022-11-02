# In this file, we define download_model
# It runs during container build time to get model weights built into the container

import boto3
import os

def download_model():
    # Download the weights from s3 (can be changed to download weights from any cloud)
    os.makedirs("dreambooth_weights/")
    s3 = boto3.resource(service_name='s3', region_name='AWS_REGION', aws_access_key_id='AWS_ACCESS_KEY', aws_secret_access_key='AWS_SECRET_ACCESS_KEY')
    bucket = s3.Bucket("BUCKET_NAME")
    for obj in bucket.objects.filter(Prefix="FOLDER_NAME"):
        target = os.path.join("dreambooth_weights/", os.path.relpath(obj.key, "FOLDER_NAME"))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == '/':
            continue
        bucket.download_file(obj.key, target)

if __name__ == "__main__":
    download_model()
