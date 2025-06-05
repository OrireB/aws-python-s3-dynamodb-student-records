import boto3

dynamodb = boto3.client('dynamodb')

# Define the student record
student = {
    'StudentID': {'S': 'S12345'},
    'Name': {'S': 'Grace Joseph'},
    'Email': {'S': 'grace.joseph@testing.com'}
}

# Insert the record
try:
    response = dynamodb.put_item(
        TableName='Students',
        Item=student,
        ReturnConsumedCapacity='TOTAL'
    )
    print("Student record inserted successfully.")
    print("Consumed capacity:", response.get('ConsumedCapacity'))
except Exception as e:
    print("Error inserting student record:", e)
