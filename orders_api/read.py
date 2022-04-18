import os
import boto3
import simplejson as json
from boto3.dynamodb.conditions import Key


dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get("ORDERS_TABLE")

def lambda_handler(event, context):
    # order = {"id": 1, "itemName": "Bugatti", "price" : 140000000}
    table = dynamodb.Table(table_name)
    order_id = int(event['pathParameters']['id'])
    response = table.query(KeyConditionExpression=Key('id').eq(order_id))
        
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }