import unittest
from unittest.mock import patch, MagicMock
from minioClient import Read_Data_Of_Exist_Object, BUCKET_NAME

class TestReadDataOfExistObject(unittest.TestCase):

    @patch('minioClient.s3')
    def test_read_existing_object(self, mock_s3):
        """Checking when the file exists and the data is read successfully"""
        mock_body = MagicMock()
        mock_body.read.return_value = b'Hello from test!'
        mock_response = {'Body': mock_body}

        mock_s3.get_object.return_value = mock_response

        Read_Data_Of_Exist_Object("testfile.txt")

        mock_s3.get_object.assert_called_once_with(Bucket=BUCKET_NAME, Key="testfile.txt")

    @patch('minioClient.s3')
    def test_object_does_not_exist(self, mock_s3):
        """Checking when the file does not exist – NoSuchKey"""
        class NoSuchKey(Exception): 
            pass
        mock_s3.exceptions = MagicMock()
        mock_s3.exceptions.NoSuchKey = NoSuchKey
        mock_s3.get_object.side_effect = NoSuchKey("Key not found")

        Read_Data_Of_Exist_Object("missing.txt")

        mock_s3.get_object.assert_called_once_with(Bucket=BUCKET_NAME, Key="missing.txt")

    @patch('minioClient.s3')
    def test_general_exception(self, mock_s3):
        """Checking when a general error is received"""
        mock_s3.get_object.side_effect = Exception("Connection failed")

        Read_Data_Of_Exist_Object("anyfile.txt")

        mock_s3.get_object.assert_called_once_with(Bucket=BUCKET_NAME, Key="anyfile.txt")

if __name__ == '__main__':
    unittest.main()
