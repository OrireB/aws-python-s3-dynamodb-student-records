import boto3

dynamodb = boto3.client('dynamodb')

try:
    response = dynamodb.create_table(
        TableName='Students',
        KeySchema=[
            {
                'AttributeName': 'StudentID',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'StudentID',
                'AttributeType': 'S'  # 'S' = String
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print("Table created. Status:", response['TableDescription']['TableStatus'])
except Exception as e:
    print("Error creating table:", e)

