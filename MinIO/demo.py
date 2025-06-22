from dotenv import load_dotenv
from minio import Minio
from io import BytesIO
import random
import string
import logging
import os

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

access = os.getenv('MINIO_ACCESS_KEY')
secret = os.getenv('MINIO_SECRET_KEY')
bucket_name = os.getenv('MINIO_BUCKET')

client = Minio( "host.docker.internal:9000",access_key=access, secret_key=secret, secure=False)

object_name = ''.join(random.choices(string.ascii_lowercase, k=8)) + ".txt"
data_str = f"Random content: {random.randint(1, 100)}"
data = data_str.encode("utf-8")

if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

client.put_object(bucket_name, object_name, BytesIO(data), length=len(data))
logger.info(f"Uploaded: {object_name}")

objects = client.list_objects(bucket_name)
for obj in objects:
        logger.info(" -", obj.object_name)

resp = client.get_object(bucket_name, object_name)
logger.info("Content:", resp.read().decode())

updated_data = b"UPDATED content goes here"

client.put_object(
    bucket_name,          
    object_name,
    data=BytesIO(updated_data),
    length=len(updated_data)
)

logger.info("Object updated successfully.")

client.remove_object(bucket_name, object_name)
logger.info(f"Deleted: {object_name}")
