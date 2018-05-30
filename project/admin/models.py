from project.models import dynamodb
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr


def check_user(email, password):
    table = dynamodb.Table('auth_users')

    try:
        response = table.query(
            KeyConditionExpression=Key('email').eq(email)
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response["Items"]
        if item:
            return item[0]['password'] == password and item[0]['email'] == email
