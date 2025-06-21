from __future__ import annotations

import logging
import random
import string
from datetime import datetime
import os
from dotenv import load_dotenv
import boto3

# --------------------------------------------------------------------------- #
# Load environment variables from .env file
# --------------------------------------------------------------------------- #
load_dotenv()

# --------------------------------------------------------------------------- #
# Logging
# --------------------------------------------------------------------------- #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# --------------------------------------------------------------------------- #
# MinIO connection details
# --------------------------------------------------------------------------- #
MINIO_ENDPOINT_URL = os.getenv("MINIO_ENDPOINT_URL")
MINIO_ACCESS_KEY_ID = os.getenv("MINIO_ACCESS_KEY_ID")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")

# S3‑compatible client (verify=False → plain HTTP, dev only)
s3 = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT_URL,
    aws_access_key_id=MINIO_ACCESS_KEY_ID,
    aws_secret_access_key=MINIO_SECRET_KEY,
    verify=False,
)

# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def create_bucket_if_not_exists(bucket: str) -> None:
    """Create *bucket* if it does not already exist."""
    try:
        s3.head_bucket(Bucket=bucket)
        logging.info("Bucket '%s' already exists.", bucket)
    except s3.exceptions.NoSuchBucket:
        s3.create_bucket(Bucket=bucket)
        logging.info("Bucket '%s' created.", bucket)
    except Exception as err:  # noqa: BLE001  (generic for demo simplicity)
        logging.error("Error checking/creating bucket '%s': %s", bucket, err)
        raise


def random_string(length: int = 15) -> str:
    """Return random lowercase‑letters‑and‑digits string of *length*."""
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))


# --------------------------------------------------------------------------- #
# CRUD
# --------------------------------------------------------------------------- #
def create_random_object() -> str:
    """Create an object with random name + data; return its key."""
    key = f"file_{datetime.now():%Y%m%d%H%M%S}_{random_string(8)}.txt"
    body = (
        f"Created at {datetime.now().isoformat()}\n"
        f"Random data: {random_string(50)}"
    )
    s3.put_object(Bucket=MINIO_BUCKET_NAME, Key=key, Body=body)
    logging.info("Object '%s' created and uploaded.", key)
    return key


def list_objects() -> None:
    """Log all objects currently in the bucket."""
    resp = s3.list_objects_v2(Bucket=MINIO_BUCKET_NAME)
    if "Contents" in resp:
        for obj in resp["Contents"]:
            logging.info(" - %s (%s bytes)", obj["Key"], obj["Size"])
    else:
        logging.info("Bucket is empty.")


def read_object(key: str) -> str:
    """Read object *key* and log its contents."""
    resp = s3.get_object(Bucket=MINIO_BUCKET_NAME, Key=key)
    data = resp["Body"].read().decode()
    logging.info("Content of '%s':\n%s", key, data)
    return data


def delete_object(key: str) -> None:
    """Delete object *key* from the bucket."""
    s3.delete_object(Bucket=MINIO_BUCKET_NAME, Key=key)
    logging.info("Object '%s' deleted.", key)


def update_object(key: str) -> None:
    """Overwrite object *key* with new content (creates new version if enabled)."""
    new_body = f"Updated at {datetime.now().isoformat()} — new content!"
    s3.put_object(Bucket=MINIO_BUCKET_NAME, Key=key, Body=new_body)
    logging.info("Object '%s' updated.", key)
    logging.info(
        "If versioning is enabled, the previous version is retained for recovery."
    )


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    create_bucket_if_not_exists(MINIO_BUCKET_NAME)

    obj1 = create_random_object()
    obj2 = create_random_object()
    obj3 = create_random_object()

    logging.info("Objects currently in bucket:")
    list_objects()

    read_object(obj1)

    delete_object(obj3)
    update_object(obj1)

    logging.info("Objects after deletion and update:")
    list_objects()
