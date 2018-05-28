import boto3, json, decimal
from botocore.exceptions import ClientError

# For a Boto3 client.
ddb = boto3.resource(
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
    response = ddb.list_tables()
    print(response)


def create_table():
    table = ddb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table status:", table.table_status)


def create_movie():
    table = ddb.Table('Movies')
    table.put_item(
        Item={
            'year': 2012,
            'title': "2012",
            'info': "Abstraction",
        }
    )


def get_movie():
    table = ddb.Table('Movies')

    title = "Abstraction"
    year = 2012

    try:
        response = table.get_item(
            Key={
                'year': year,
                'title': title
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['ResponseMetadata']
        print("GetItem succeeded:")
        print(json.dumps(item, indent=4, cls=DecimalEncoder))


get_movie()
