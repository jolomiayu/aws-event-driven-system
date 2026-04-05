import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        message = body['message']

        print(f"Processing message: {message}")

        # Save to DynamoDB
        table.put_item(
            Item={
                'id': str(uuid.uuid4()),
                'message': message
            }
        )

        # Simulate failure
        if message == "fail":
            raise Exception("Simulated failure")

    return {
        'statusCode': 200
    }
