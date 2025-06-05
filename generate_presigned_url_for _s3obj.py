import boto3

s3 = boto3.client('s3')

# Bucket and file details
bucket_name = 'success-guaranteed'
object_key = 'Fierce.jpeg'

try:
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': object_key},
        ExpiresIn=3600
    )
    print("Pre-signed URL (valid for 1 hour):")
    print(url)
except Exception as e:
    print("Failed to generate pre-signed URL:", e)
