import json
import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    # 1. Get the file name from the S3 event
    try:
        file_name = event['Records'][0]['s3']['object']['key']
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        
        print(f"File detected: {file_name}")

        # 2. YOUR TOPIC ARN (From your screenshot)
        topic_arn = 'arn:aws:sns:eu-central-1:376505902429:PortfolioAlerts'

        # 3. Create the message
        message_text = f"🚀 Alert! A new file '{file_name}' was just uploaded to your portfolio bucket ({bucket_name})."
        
        # 4. Publish to SNS
        response = sns.publish(
            TopicArn=topic_arn,
            Subject='New Portfolio Update',
            Message=message_text
        )
        print("Message sent to SNS!")
        return "Success"
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise e