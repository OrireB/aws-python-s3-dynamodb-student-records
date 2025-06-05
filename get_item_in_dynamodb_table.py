import boto3

dynamodb = boto3.client('dynamodb')

try:
    response = dynamodb.get_item(
        TableName='Students',
        Key={'StudentID': {'S': 'S12345'}}
    )
    print("Student record retrieved successfully:")
    print(response['Item'])
except Exception as e:
    print("Error retrieving student record:", e)
