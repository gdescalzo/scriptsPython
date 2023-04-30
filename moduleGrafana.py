""" Import Module / method """
import requests
import json
import base64

""" Create Grafana organization """
def create_grafana_org(grafana_vars, grafana_org_name, grafana_user, grafana_password):
    try:
        grafana_fqdn = grafana_vars['grafana_fqdn']
        grafana_endpoint_create_org = grafana_vars['grafana_endpoint_create_org']

        grafana_url = grafana_fqdn + grafana_endpoint_create_org
        payload = json.dumps({"name": grafana_org_name})
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {base64.b64encode((grafana_user + ':' + grafana_password).encode()).decode()}"
        }

        response = requests.post(grafana_url, headers=headers, data=payload)
        response.raise_for_status() # raise exception if request failed with a 4xx or 5xx status code
        grafana_org_output = response.json()
        grafana_org_output_message = grafana_org_output['message']
        grafana_org_id = grafana_org_output['orgId']
        
        return grafana_org_output_message, grafana_org_id

    except Exception as e:
        print("An error occurred while creating a Grafana organization:", e)

""" Create Grafana Token """
def create_grafana_token(grafana_vars, grafana_user, grafana_password, grafana_org_name, grafana_org_id):
    try:
        grafana_fqdn = grafana_vars['grafana_fqdn']
        grafana_endpoint_create_token = grafana_vars['grafana_endpoint_create_token']
        grafana_org_token_role = grafana_vars['grafana_org_token_role']

        grafana_url = grafana_fqdn + grafana_endpoint_create_token
        payload = json.dumps({
            "name": grafana_org_name,
            "role": grafana_org_token_role
        })
        headers = {
            'Content-Type': 'application/json',
            "Authorization": f"Basic {base64.b64encode((grafana_user + ':' + grafana_password).encode()).decode()}",
            "X-Grafana-Org-Id": str(grafana_org_id)
        }

        response = requests.post(grafana_url, headers=headers, data=payload)
        # raise exception if request failed with a 4xx or 5xx status code
        response.raise_for_status()
        response_json = response.json()
        token = (response_json['key'])

        return token

    except Exception as e:
        print("An error occurred while creating a Grafana token:", e)

""" Get Grafana Folder list """
def get_grafana_org_folders(grafana_vars, grafana_keyvault_secret_value):
    try:
        grafana_fqdn = grafana_vars['grafana_fqdn']
        grafana_endpoint_get_folder = grafana_vars['grafana_endpoint_get_folder']

        grafana_url = grafana_fqdn + grafana_endpoint_get_folder
        payload = ""
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + grafana_keyvault_secret_value,
        }

        response = requests.request(
            "GET", grafana_url, headers=headers, data=payload)
        # raise exception if request failed with a 4xx or 5xx status code
        response.raise_for_status()
        response_json = response.json()
        grafana_folder_list = (response_json[0]['title'])

        return grafana_folder_list

    except Exception as e:
        print("An error occurred while retrieving Grafana organization folders:", e)

""" Create Grafana Folder """
def create_grafana_org_folders(grafana_vars, grafana_org_app_folder_name, grafana_keyvault_secret_value):
    try:
        grafana_fqdn = grafana_vars['grafana_fqdn']
        grafana_endpoint_create_folder = grafana_vars['grafana_endpoint_create_folder']

        grafana_url = grafana_fqdn + grafana_endpoint_create_folder
        payload = json.dumps({
            "title": grafana_org_app_folder_name,
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + grafana_keyvault_secret_value
        }

        response = requests.post(grafana_url, headers=headers, data=payload)
        # raise exception if request failed with a 4xx or 5xx status code
        response.raise_for_status()

        return response.text

    except Exception as e:
        print("An error occurred while creating Grafana organization folder:", e)

""" Create Grafana Data Source """
def create_grafana_datasource(sre_spn_credentials, grafana_vars, grafana_org_name, grafana_org_id, grafana_keyvault_secret_value, azure_subscription_id, grafana_org_app_folder_name):
    try:
        grafana_datasource_name = grafana_org_name + " - " + grafana_org_app_folder_name
        grafana_fqdn = grafana_vars['grafana_fqdn']
        grafana_endpoint_create_datasource = grafana_vars['grafana_endpoint_create_datasource']

        client_id = sre_spn_credentials['client_id']
        client_secret = sre_spn_credentials['client_secret']
        tenant_id = sre_spn_credentials['tenant_id']

        grafana_url = grafana_fqdn + grafana_endpoint_create_datasource
        payload = json.dumps({
            "name": grafana_datasource_name,
            "type": "grafana-azure-monitor-datasource",
            "access": "proxy",
            "orgId": grafana_org_id,
            "jsonData": {
                "azureAuthType": "clientsecret",
                "clientId": client_id,
                "cloudName": "azuremonitor",
                "subscriptionId": azure_subscription_id,
                "tenantId": tenant_id
                },
            "secureJsonData": {
                "clientSecret": client_secret
                }
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + grafana_keyvault_secret_value
        }
        response = requests.post(grafana_url, headers=headers, data=payload)
        # raise exception if request failed with a 4xx or 5xx status code
        response.raise_for_status()

        return response.text
    
    except Exception as e:
        print("An error occurred while creating Grafana organization folder:", e)

""" Add Grafana SRE users 
def add_grafana_sre_users(grafana_vars, sre_user_list, grafana_keyvault_secret_value):
    try:
        grafana_fqdn = grafana_vars['grafana_fqdn']
        grafana_endpoint_adduser = grafana_vars['grafana_endpoint_adduser']
        grafana_url = grafana_fqdn + grafana_endpoint_adduser

        for user in sre_user_list:

            payload = json.dumps({
                "role": "admin",
                "loginOrEmail": user
            })
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + grafana_keyvault_secret_value
            }
            response = requests.post(grafana_url, headers=headers, data=payload)
            # raise exception if request failed with a 4xx or 5xx status code
            response.raise_for_status()

            return response.text

    except Exception as e:
        print("An error occurred while creating Grafana organization folder:", e)

"""