"""This script demonstrates how to use the MinIO Python client to interact with a MinIO server."""
import string as st
import random as rd
import io
from minio import Minio
from minio.error import S3Error
from dotenv import load_dotenv
import os
import logging


load_dotenv()  

client_minio=Minio("minio:9000",
   access_key=os.getenv("ACCESS_KEY"),
   secret_key=os.getenv("SECRET_KEY"),
   secure=False)
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()

console_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
def rand_data ():
    """Generate random data for testing."""
    return(''.join(rd.choices(st.printable, k=rd.randint(10,50))))

def rand_name ():
    """Generate a random name for the object."""    
    return(''.join(rd.choices(st.ascii_letters, k=7)))

bucket_name = "my-bucket"
object_name = rand_name()

def add_object (bucket_name = "my-bucket",object_name = rand_name()):
    """Add an object to the specified bucket."""    
    data_to_upload = rand_data().encode('utf-8')
    """Make sure the bucket exists"""
    found = client_minio.bucket_exists(bucket_name)
    if not found:
        client_minio.make_bucket(bucket_name)
    try:
        client_minio.put_object(
            bucket_name,
            object_name,
            io.BytesIO(data_to_upload),
            len(data_to_upload),
            content_type="text/plain"
        )
        logger.info(f"'{object_name}' uploaded successfully to '{bucket_name}'.")
    except S3Error as exc:
        logger.error(f"Error uploading object: {exc}")
    return bucket_name, object_name
def list_objects(bucket_name):
    """List all objects in the specified bucket."""
    logger.info(f"Objects in bucket '{bucket_name}':")
    for obj in client_minio.list_objects(bucket_name):
        logger.info(f" - {obj.object_name} (size: {obj.size} bytes, last modified: {obj.last_modified})")
    
def get_object(bucket_name, object_name):
    """Retrieve an object from the specified bucket."""
    try:
        response = client_minio.get_object(bucket_name, object_name)
        logger.info(f"Data from '{object_name}': {response.read().decode('utf-8')}")
    except S3Error as exc:
        logger.error(f"Error retrieving object: {exc}")
def delete_object(bucket_name, object_name):
    """Delete an object from the specified bucket."""
    try:
        client_minio.remove_object(bucket_name, object_name)
        logger.info(f"'{object_name}' removed successfully from '{bucket_name}'.")
    except S3Error as exc:
        logger.error(f"Error removing object: {exc}")
def update_object(bucket_name, object_name):
    """Update an existing object in the specified bucket."""
    new_data = rand_data().encode('utf-8')
    try:
        client_minio.put_object(
            bucket_name,
            object_name,
            io.BytesIO(new_data),
            len(new_data),
            content_type="text/plain"
        )
        logger.info(f"'{object_name}' updated successfully in '{bucket_name}'.")
        print("When updating an existing object in a system that uses versioning, " \
        "the update typically creates a new version of the object rather than overwriting " \
        "the existing one. This preserves the previous state of the object, allowing for easy recovery "
        "if the update is flawed or unintended.")
    except S3Error as exc:
        logger.error(f"Error updating object: {exc}")
add_object(bucket_name, object_name)
list_objects(bucket_name)
get_object(bucket_name, object_name)
delete_object(bucket_name, object_name)
list_objects(bucket_name)
update_object(bucket_name, object_name)
list_objects(bucket_name)

