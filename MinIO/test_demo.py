import unittest
from minio import Minio
from io import BytesIO
import os
from dotenv import load_dotenv

load_dotenv()

class TestMinIO(unittest.TestCase):
    def setUp(self):
        self.client = Minio(
            "host.docker.internal:9000",
            access_key=os.getenv('MINIO_ACCESS_KEY'),
            secret_key=os.getenv('MINIO_SECRET_KEY'),
            secure=False
        )
        self.bucket = os.getenv('MINIO_BUCKET')
        self.object_name = "test_object.txt"
        self.data = b"Test content"

        if not self.client.bucket_exists(self.bucket):
            self.client.make_bucket(self.bucket)

    def test_upload_get_and_delete(self):
        self.client.put_object(
            self.bucket,
            self.object_name,
            BytesIO(self.data),
            len(self.data)
        )

        obj = self.client.get_object(self.bucket, self.object_name)
        content = obj.read()
        self.assertEqual(content, self.data)

        self.client.remove_object(self.bucket, self.object_name)

        with self.assertRaises(Exception):  
            self.client.get_object(self.bucket, self.object_name)

if __name__ == "__main__":
    unittest.main()
