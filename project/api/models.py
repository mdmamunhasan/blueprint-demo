from project.models import dynamodb
from botocore.exceptions import ClientError


def get_users():
    table = dynamodb.Table('auth_users')

    try:
        response = table.scan()
    except ClientError as ex:
        print(ex.response['Error']['Message'])
    else:
        item = response["Items"]
        return item
