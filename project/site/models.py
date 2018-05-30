from project.models import dynamodb
from botocore.exceptions import ClientError


def create_user(username, password, email):
    table = dynamodb.Table('auth_users')

    try:
        response = table.put_item(
            Item={
                'email': email,
                'username': username,
                'password': password
            },
            ConditionExpression="(attribute_not_exists(email))"
        )
    except ClientError as ex:
        print(ex.response['Error']['Message'])
    else:
        return response
