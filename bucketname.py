# https://realpython.com/python-boto3-aws-s3/

import uuid
import boto3

def create_bucket_name(bucket_name):
     return ''.join([bucket_name,str(uuid.uuid4())])
# You need to provide both a bucket name and a bucket configuration where you must specify the region
s3_resource.create_bucket(Bucket=bucket_name,
                          CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

# AUTOMATIC
def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

# Creating random file name
def random_filename(size,filename,file_content):
    rand=''.join([str(uuid.uuid4().hex[:6]),filename])
    with open(rand,'w') as f:
        f.write(str(file_content)*size)
    return rand
random_filename(300,'mohan.txt','f')

# creating and adding object to that.
first_bucket = s3_resource.Bucket(name=first_bucket_name)
first_object = s3_resource.Object(
    bucket_name=first_bucket_name, key=first_file_name)

# Addind files to s3 bucket
import boto3
s3 = boto3.client('s3')
s3.upload_file('name_of_file','bucket_name','name_you_want_to_Save')

# Downloading files from s3 bucket
s3_resource.Object(first_bucket_name, first_file_name).download_file(
    f'/tmp/{first_file_name}')

# Copying from one bucket to another bucket
def copy_to_bucket(bucket_from_name, bucket_to_name, file_name):
    copy_source = {
        'Bucket': bucket_from_name,
        'Key': file_name
    }
    s3_resource.Object(bucket_to_name, file_name).copy(copy_source)

copy_to_bucket(first_bucket_name, second_bucket_name, first_file_name)

# Deleting an object
s3_resource.Object(second_bucket_name, first_file_name).delete()


