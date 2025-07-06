import json
import boto3
import base64
import uuid
import os
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

BUCKET_NAME = os.environ['BUCKET_NAME']
TABLE_NAME = os.environ['DYNAMODB_TABLE']

def upload_image(event, context):
    try:
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
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(
            Item={
                'id': image_id,
                'filename': filename,
                'timestamp': timestamp,
                'created_at': datetime.now().isoformat()
            }
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST'
            },
            'body': json.dumps({
                'success': True,
                'image_id': image_id,
                'url': f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"
            })
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST'
            },
            'body': json.dumps({
                'success': False,
                'error': str(e)
            })
        }