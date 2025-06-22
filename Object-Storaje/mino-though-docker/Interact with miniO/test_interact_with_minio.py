import sys
import os
import logging

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from Interact_with_miniO import (
    create_bucket_if_not_exists,
    create_random_object,
    update_object,
    list_objects,
    read_object,
    MINIO_BUCKET_NAME,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Checking if bucket exists and creating it if not.")

# if bucket created
create_bucket_if_not_exists(MINIO_BUCKET_NAME)

key = create_random_object()

# if object created
if key:
    logging.info("Successfully created object with key: %s", key)
else:
    logging.error("Failed to create object.")

logging.info("Uploading file to bucket.")
update_object(key)

logging.info("Reading object from bucket.")
read_object(key)

logging.info("Contents of the bucket:")
list_objects()
