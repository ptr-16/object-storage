import unittest
import uuid
from Code import s3, BUCKET_NAME, list_objects, read_object, remove_object, update_object
class TestS3Functions(unittest.TestCase):
    
    def setUp(self):
        self.test_key = str(uuid.uuid4()) + '.txt'
        self.test_data = 'ABC123'
        s3.put_object(Bucket=BUCKET_NAME, Key=self.test_key, Body=self.test_data)
    def test_list_objects(self):
      try:
            list_objects(BUCKET_NAME)
      except Exception as e:
            self.fail(f"Error displaying object list: {e}")
    def test_read_object(self):
        try:
            read_object(BUCKET_NAME,self.test_key)
        except Exception as e:
            self.fail(f"Error reading file {e}")  
    def test_remove_object(self):
        try:
            remove_object(BUCKET_NAME,self.test_key)
        except Exception as e:
            self.fail(f"Error deleting file{e}")  
if __name__ == '__main__':
  unittest.main()