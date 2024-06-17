import boto3
import json

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

# Initialize the AWS Health client
client = boto3.client('health', 
                      region_name="us-east-1", # should use the global endpoint, which is health.us-east-1.amazonaws.com
                      aws_access_key_id=access_key, 
                      aws_secret_access_key=secret_access_key)

def check_ses_health():
    # Get the AWS Health events
    response = client.describe_events(filter={'services': ['SES']})
    # Print the response
    for event in response['events']:
        print(f"Service: {event['service']}")
        print(f"Event Type Code: {event['eventTypeCode']}")
        print(f"Event Type Category: {event['eventTypeCategory']}")
        print(f"Region: {event['region']}")
        print(f"Start Time: {event['startTime']}")
        print(f"Last Updated Time: {event['lastUpdatedTime']}")
        print(f"Status Code: {event['statusCode']}")
        print("\n")

# Call the function to check the SES health
check_ses_health()