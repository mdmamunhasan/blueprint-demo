import boto3, json, decimal
from botocore.exceptions import ClientError

# For a Boto3 client.
ddbclient = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='ap-southeast-1',
    aws_access_key_id='anything',
    aws_secret_access_key='anything'
)

dynamodb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='ap-southeast-1',
    aws_access_key_id='anything',
    aws_secret_access_key='anything'
)


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


def list_tables():
    response = ddbclient.list_tables()
    print(response)


def create_table():
    table = dynamodb.create_table(
        TableName='auth_users',
        KeySchema=[
            {
                'AttributeName': 'email',
                'KeyType': 'HASH'  # Partition key
            }

        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'email',
                'AttributeType': 'S'
            }

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table status:", table.table_status)


list_tables()
