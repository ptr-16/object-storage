
#8.//Write *client* code, in any language, to interact with the MinIO instance.
import boto3
import uuid
import random
import string
from dotenv import load_dotenv
import os
import logging
logging.basicConfig(level=logging.INFO)
import unittest
load_dotenv()

ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
BUCKET_NAME = os.getenv("BUCKET_NAME")

s3 = boto3.client(
    's3',
    endpoint_url=ENDPOINT_URL,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
#Randomly create new object 
try:
    s3.create_bucket(Bucket=BUCKET_NAME)
except s3.exceptions.BucketAlreadyOwnedByYou:
    pass

my_random_object_name=str(uuid.uuid4()) + '.txt'
my_random_object_data=''.join(random.choices(string.ascii_letters, k=20))
s3.put_object(Bucket=BUCKET_NAME, Key=my_random_object_name, Body=my_random_object_data)
#List the existing objects.
def list_objects(bucket_name):
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        contents = response.get('Contents', [])
        if not contents:
            logging.info("The bucket is empty.")
        else:
            logging.info("Objects in bucket:")
            for obj in contents:
                logging.info(f"- {obj['Key']}")
    except Exception as e:
        logging.info(f"Error listing objects in bucket '{bucket_name}': {e}")
#Read the data of an existing object.
def read_object(bucket_name, key_name):
    try:
        response = s3.get_object(Bucket=bucket_name, Key=key_name)
        content = response['Body'].read().decode('utf-8')
        logging.info("Object content:")
        logging.info(content)
    except s3.exceptions.NoSuchKey:
        logging.info(f"Error: The key '{key_name}' does not exist in bucket '{bucket_name}'.")
    except Exception as e:
        logging.info(f"Failed to read object: {e}")


def remove_object(bucket_name, key_name):
    try:
        s3.delete_object(Bucket=bucket_name, Key=key_name)
        logging.info(f"the object'{key_name}' remove from the bucket'{bucket_name}'")
    except s3.exceptions.NoSuchKey:
        logging.info(f"the file:'{key_name}' not found in the bucket'{bucket_name}'")
    except Exception:
        logging.info("Error deleting file from bucket")
#Update an existing object 
def update_object(KeyName, BucketName):
    """
    When updating a file, each update saves a new version of the object, 
    if 'versioning' is enabled,
    so that previous versions can be restored.
    """
    try:
        s3.put_object(Bucket=BucketName, Key=KeyName, Body='update content')
        logging.info(f"the file:'{KeyName}'Updated successfully'{BucketName}'")
        s3.get_bucket_versioning(Bucket=BucketName)
        logging.info(f"The file '{KeyName}' was updated successfully in bucket '{BucketName}'.")
    except Exception as e:
        logging.info(f"Error updating file from bucket {e}")
#Summoning functions      
list_objects(BUCKET_NAME)
read_object(BUCKET_NAME, "some_object_key.txt")
update_object("some_object_key.txt", BUCKET_NAME)
remove_object(BUCKET_NAME, "some_object_key.txt")   
