import boto3
import uuid
import random
import string
import os
import logging

s3 = boto3.client(
    's3',
   endpoint_url='http://minio:9000',
    aws_access_key_id='admin',
    aws_secret_access_key='admin123',
)

BUCKET_NAME='riki'
OBJECT_KEY='HI.txt'
Objeckt_Key_Update='HELLO.txt'
LOCAL_FILE_PATH = os.path.join("temp", Objeckt_Key_Update)
N=5
logging.basicConfig(level=logging.INFO)

def Create_Object():
    """"create a random files"""
    try:
        os.makedirs("temp", exist_ok=True)
        for i in range(0,N):
            filename = f"{uuid.uuid4()}.txt"
            OBJECT_KEY = filename
            LOCAL_FILE_PATH =  os.path.join("temp", OBJECT_KEY)
            with open(LOCAL_FILE_PATH, "w") as f:
                f.write(''.join(random.choices(string.ascii_letters + string.digits, k=80)))
            s3.upload_file(LOCAL_FILE_PATH, BUCKET_NAME, OBJECT_KEY)
        logging.info("it uplaod well")
    except Exception as e:
         logging.info(f"An error occurred: {e}")
        
#1.
def List_Exsit_Object():
    """give the list of the Object"""
    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            logging.info(f"Objects in bucket '{BUCKET_NAME}':")
            for obj in response['Contents']:
                logging.info(f"  - {obj['Key']} (Size: {obj['Size']} bytes, Last Modified: {obj['LastModified']})")
        else:
            logging.info(f"No objects found in bucket '{BUCKET_NAME}'.")
    except Exception as e:
        logging.info(f"An error occurred: {e}")

# 2.
def Read_Data_Of_Exist_Object(OBJECT_KEY):
    """read the data from exist object"""
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
        object_data = response['Body'].read()
        logging.info(f"Object data: {object_data.decode('utf-8')}") # Decode if it's text
    except s3.exceptions.NoSuchKey:
        logging.info(f"Object '{OBJECT_KEY}' not found in bucket '{BUCKET_NAME}'.")
    except Exception as e:
        logging.info(f"An error occurred: {e}")

#3
def Remove_Exist_Object(OBJECT_KEY):
    """remove exist object"""
    try:
        s3.delete_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
        logging.info(f"Object '{OBJECT_KEY}' successfully deleted from bucket '{OBJECT_KEY}'.")
    except Exception as e:
        logging.info(f"Error deleting object: {e}")    

#4
def Update_an_existing_object(Objeckt_Key_Update,LOCAL_FILE_PATH):
    """updata the exist object"""
    try:
        new_content = "This is the updated content for the object."
        s3.put_object(Bucket=BUCKET_NAME, Key=Objeckt_Key_Update, Body=new_content.encode('utf-8'))
        logging.info(f"Object '{Objeckt_Key_Update}' in bucket '{BUCKET_NAME}' updated successfully with new content.")
    except Exception as e:
        logging.info(f"Error updating object: {e}")

#Summoning the methods
Create_Object()
List_Exsit_Object()
Read_Data_Of_Exist_Object(OBJECT_KEY)
Remove_Exist_Object(OBJECT_KEY)
Update_an_existing_object(Objeckt_Key_Update,LOCAL_FILE_PATH)
