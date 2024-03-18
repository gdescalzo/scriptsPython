import os
import json
import pandas as pd
from datetime import datetime
from azure.identity import ClientSecretCredential
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.subscription import SubscriptionClient

# Authenticate the client
def authenticate_client(tenant_id, client_id, client_secret):
    credentials = ClientSecretCredential(
        tenant_id=tenant_id,
        client_id=client_id,
        client_secret=client_secret
    )
    return credentials

# Get the subscription id
def get_subscription_id(credentials, subscription_name):
    # Create a client
    client = SubscriptionClient(credentials)

    # Get all subscriptions
    subscriptions = client.subscriptions.list()

    # Search for the subscription with the provided name
    for subscription in subscriptions:
        if subscription.display_name == subscription_name:
            return subscription.subscription_id

    # If no subscription with the provided name is found, return None
    return None

# Get Metric alerts
def get_metric_alerts(subscription_id, subscription_name, credentials,alert_pattern, dataframe):
    # Create a client
    client = MonitorManagementClient(credentials, subscription_id)

    # Get all metric alerts
    alerts = client.metric_alerts.list_by_subscription()
    for alert in alerts:
        if alert.name.startswith(alert_pattern):
            new_row = pd.DataFrame({
                'Subscription Name': [subscription_name],
                'Subscription ID': [subscription_id],
                'Alert Resource Group': [alert.scopes[0].split('/')[4]],
                'Azure Resource Type': [alert.type],
                'Alert Name': [alert.name],
                'Alert Location': [alert.location],
                'Alert Severity': [alert.severity],
                'Alert Enabled': [alert.enabled],
                'Alert Description': [alert.description],
                'Alert Evaluation Frequency': [alert.evaluation_frequency.total_seconds() / 60],
                'Alert Window Size': [alert.window_size.total_seconds() / 60],
                'Alert Scope': [alert.scopes[0].split('/')[8]],
                'Alert Resource Type': [alert.target_resource_type],
                'Alert Query Type': ['N/A'],
                'Query': ['N/A'],
            })
            dataframe = pd.concat([dataframe, new_row], ignore_index=True)
    return dataframe

# Get Log Alerts
def get_log_query_alerts(subscription_id, subscription_name, credentials, alert_pattern, dataframe):
    # Create a client
    client = MonitorManagementClient(credentials, subscription_id)

    # Get all log query alerts
    alerts = client.scheduled_query_rules.list_by_subscription()

    for alert in alerts:
        if alert.name.startswith(alert_pattern):
            new_row = pd.DataFrame({
                'Subscription Name': [subscription_name],
                'Subscription ID': [subscription_id],
                'Alert Resource Group': [alert.id.split('/')[4]],
                'Azure Resource Type': [alert.type],
                'Alert Name': [alert.name],
                'Alert Location': [alert.location],
                'Alert Severity': [alert.action.severity],
                'Alert Enabled': [alert.enabled],
                'Alert Description': [alert.description],
                'Alert Evaluation Frequency': [alert.schedule.frequency_in_minutes],
                'Alert Window Size': [alert.schedule.time_window_in_minutes],
                'Alert Scope': [alert.source.data_source_id.split('/')[8]],
                'Alert Resource Type': ['microsoft.operationalinsights/workspaces'],
                'Alert Query Type': [alert.source.query_type],
                'Query': [alert.source.query],
            })

            dataframe = pd.concat([dataframe, new_row], ignore_index=True)

    return dataframe

# Get subscription list
def list_subscriptions_by_name(credentials, subscription_pattern):
    # Create a client
    client = SubscriptionClient(credentials)

    # Get all subscriptions
    subscriptions = client.subscriptions.list()

    # Create a list to store the subscriptions
    subscription_names = []

    # Loop through each subscription
    for subscription in subscriptions:
        # Check if the pattern is in the display name of the subscription and exclude the "NON" subscriptions list that normaly are related to "NON-PROD" environments.
        if subscription_pattern in subscription.display_name and "NON" not in subscription.display_name:
            # Add subscription name to the list instead of printing it
            subscription_names.append(subscription.display_name)

    # Return the list of subscription names
    return subscription_names

# Load credentials:
tenant_id = os.getenv('AZURE_TENANT_ID')
client_id = os.getenv('AZURE_CLIENT_ID')
client_secret = os.getenv('AZURE_CLIENT_SECRET')

# Get credentials using service principal
credentials = authenticate_client(tenant_id, client_id, client_secret)

# Please input the Azure Alerts Pattern
#alert_pattern = 'sre-eymp-ap-'
alert_pattern = os.getenv('ALERT_PATTERN')

# Please input the Azure Subscription Pattern
#suscription_pattern = 'TAX-EYMP'
subscription_pattern = os.getenv('SUBSCRIPTION_PATTERN')

# Please input the Excel file name
#excel_file_name_export = 'output.xlsx'
excel_file_name_export = os.getenv('EXCEL_FILE_NAME')

# Get the subscription list
subscription_names = list_subscriptions_by_name(credentials, subscription_pattern)

# Loop through each subscription name

# Create an empty DataFrame with columns
dataframe = pd.DataFrame(columns=["Subscription Name", "Subscription ID", "Alert Resource Group", "Azure Resource Type", "Alert Name", "Alert Location", "Alert Severity", "Alert Enabled", "Alert Description", "Alert Evaluation Frequency", "Alert Window Size", "Alert Scope", "Alert Resource Type", "Alert Query Type", "Query"])

for subscription_name in subscription_names:

    # Get the subscription ID for each subscription name
    subscription_id = get_subscription_id(credentials, subscription_name)

    # Get the metric alerts for that subscription
    dataframe = get_metric_alerts(subscription_id, subscription_name, credentials,alert_pattern, dataframe)

    # Get the log query alerts for that subscription
    dataframe = get_log_query_alerts(subscription_id, subscription_name, credentials,alert_pattern, dataframe)


# Finally, save the dataframe to file
dataframe.to_excel('./Remote_execution/output_dir/' + excel_file_name_export + '.xlsx', index=False)