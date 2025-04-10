import boto3
from datetime import datetime
 
bedrock_client = boto3.client(service_name="bedrock")
 
# Generate unique names for the job and model
job_name = f"distillation-job-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
model_name = f"distilled-model-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
 
# Configure your models and IAM role
teacher_model = "arn:aws:bedrock:us-west-2::foundation-model/meta.llama3-1-70b-instruct-v1:0"
student_model = "arn:aws:bedrock:us-west-2::foundation-model/meta.llama3-1-8b-instruct-v1:0:128k"
role_arn = "arn:aws:iam::<YOUR_ACCOUNT_ID>:role/<YOUR_IAM_ROLE>"
# Specify S3 locations for training data and output
training_data = "s3://<YOUR_BUCKET>/training-data.jsonl" # Replace by your training file
output_path = "s3://<YOUR_BUCKET>/output/" 
# Specify MaxResponseLengthForInference parameter
max_response_length = 1000