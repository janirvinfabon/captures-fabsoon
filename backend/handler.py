import json
import time
import re
import boto3
import base64
import uuid
import os
from datetime import datetime

os.environ['TZ'] = 'Asia/Manila'
if hasattr(time, 'tzset'):
    time.tzset()

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

BUCKET_NAME = os.getenv('BUCKET_NAME')
IMAGES_TABLE = os.getenv('IMAGES_TABLE')
RSVP_TABLE = os.getenv('RSVP_TABLE')

def _handle_response(status_code, body:dict = {}):
    print(json.dumps({
        "status_code": status_code,
        "body": body
    }))

    return {
        'statusCode': status_code,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS'
        },
        'body': json.dumps(body)
    }

def upload_image(event, context):
    try:
        _ = context
        body = json.loads(event['body'])
        image_data = body['image']
        timestamp = body.get('timestamp', datetime.now().isoformat())
        
        # Remove data URL prefix
        image_data = image_data.split(',')[1]
        image_bytes = base64.b64decode(image_data)
        
        # Generate unique filename
        image_id = str(uuid.uuid4())
        filename = f"souvenirs/{image_id}.jpg"
        
        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=image_bytes,
            ContentType='image/jpeg'
        )
        
        # Save metadata to DynamoDB
        table = dynamodb.Table(IMAGES_TABLE)
        table.put_item(
            Item={
                'id': image_id,
                'filename': filename,
                'timestamp': timestamp,
                'created_at': datetime.now().isoformat()
            }
        )
        
        return _handle_response(200, {
            'success': True,
            'image_id': image_id,
            'url': f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
        })
        
    except Exception as e:
        return _handle_response(500, {
            'success': False,
            'error': str(e)
        })

def rsvp_handler(event, context):
    try:
        _ = context
        body = json.loads(event['body'])
        email:str = body['email'].strip().lower()
        current_date = datetime.now().isoformat()

        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, email):
            return _handle_response(400, {
                'success': False,
                'error': 'Please provide a valid email address.'
            })

        table = dynamodb.Table(RSVP_TABLE)
        response = table.get_item(
            Key={
                'email': email
            }
        )

        rsvp_object = {
            'email': email,
            'name': body['name'].strip().title(),
            'attendance': body['attendance'],
            'timestamp': body.get('timestamp', current_date),
            'created_at': current_date,
            'stage': os.environ.get('STAGE', 'dev'),
            'created_at_gsi': datetime.now().strftime('%Y-%m-%d')
        }

        if 'Item' in response:
            rsvp_object['updated_at'] = current_date
            rsvp_object['attendance'] = body['attendance']
        
        table.put_item(
            Item=rsvp_object
        )
        
        return _handle_response(200, {
            'success': True,
            'email': email
        })
        
    except Exception as e:
        return _handle_response(500, {
            'success': False,
            'error': str(e)
        })