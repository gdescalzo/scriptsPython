import boto3
import json
from datetime import datetime

# Load the credentials from a JSON file
def load_credentials(json_filepath):
    with open(json_filepath, 'r') as f:
        data = json.load(f)

    credentials = data['credentials'][0]
    access_key = credentials['access_key']
    secret_access_key = credentials['secret_access_key']
    region_name = credentials['region_name']

    return access_key, secret_access_key, region_name

# Use the function to load credentials:
filepath = r'C:\SOME_PATH\Repos\scriptsPython\AWS\SES\Credentials.json'
access_key, secret_access_key, region_name = load_credentials(filepath)

# Initialize the Amazon SES client
client = boto3.client('ses', 
                      region_name=region_name, 
                      aws_access_key_id=access_key, 
                      aws_secret_access_key=secret_access_key)

# Set the threshold for the number of emails
threshold = 2500

def check_email_sent():
    # Get the current date
    today = datetime.now().strftime('%Y-%m-%d')

    # Get the send quota for the current date
    response = client.get_send_quota()

    # Get the number of emails sent today
    emails_sent_today = response['SentLast24Hours']

    # Check if the number of emails sent is greater than the threshold
    if emails_sent_today > threshold:
        print(f'Warning: Email threshold exceeded. {emails_sent_today} emails sent on {today}.')
    else:
        # Print the response
        print(f"Max 24 Hour Send: {response['Max24HourSend']}")
        print(f"Max Send Rate: {response['MaxSendRate']}")
        print(f"Sent Last 24 Hours: {response['SentLast24Hours']}")

# Call the function to check the number of emails sent
check_email_sent()