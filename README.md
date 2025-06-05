# AWS Python Project – S3 and DynamoDB

This is a simple Python project that interacts with two AWS services(S3 and DynamoDB using the **boto3** library:

- **Amazon S3** – to create a bucket, upload a file, and generate a pre-signed URL
- **Amazon DynamoDB** – to create a table, insert a student record, and retrieve it

The project follows official [boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) for working with AWS services in Python.

---

## This Project Does Entails:

1. **Creates an S3 bucket**
2. **Uploads a file** (like an image) to the bucket using `upload_file()`
3. **Generates a pre-signed URL** for downloading the file
4. **Creates a DynamoDB table** named `Students`
5. **Inserts a student record** using `put_item()`  
6. **Retrieves the student record** using `get_item()`

---

## How to Run this code

Make sure you have:

- Python installed
- `boto3` library installed (`pip install boto3`)
- AWS CLI configured (`aws configure`) with access keys and default region

Then run each Python script step by step.
