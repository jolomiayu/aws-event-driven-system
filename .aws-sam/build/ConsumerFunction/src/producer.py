import json
import boto3
import os

sqs = boto3.client('sqs')
QUEUE_URL = os.environ['QUEUE_URL']

def lambda_handler(event, context):
    body = json.loads(event['body'])
    
    message = body.get('message', 'No message')

    sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps({
            'message': message
        })
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Message sent to queue')
    }
