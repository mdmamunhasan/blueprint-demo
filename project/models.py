import boto3

# For a Boto3 client.
ddb = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='ap-southeast-1',
    aws_access_key_id='anything',
    aws_secret_access_key='anything'
)


def list_tables():
    response = ddb.list_tables()
    print(response)


def create_table():
    pass


list_tables()
