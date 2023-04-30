""" Import Module / method """
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

""" Getting Grafana Credentials from Azure KeyVault """
def get_grafana_credentials(sre_spn_credentials, azure_vars):
    try:
        tenant_id = sre_spn_credentials['tenant_id']
        client_id = sre_spn_credentials['client_id']
        client_secret = sre_spn_credentials['client_secret']

        azure_keyvault_grafana_user = azure_vars['azure_keyvault_grafana_user']
        azure_keyvault_grafana_password = azure_vars['azure_keyvault_grafana_password']
        azure_keyvault_sre = azure_vars['azure_keyvault_sre']

        credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
        secret_client = SecretClient(vault_url=azure_keyvault_sre, credential=credential)
        grafana_user_name = secret_client.get_secret(azure_keyvault_grafana_user).value
        grafana_password = secret_client.get_secret(azure_keyvault_grafana_password).value

        return grafana_user_name, grafana_password

    except Exception as e:
        print(f"Error occurred: {e}")
        return None, None

""" Store Grafana Credentials in Azure KeyVault """
def store_grafana_token(sre_spn_credentials, azure_vars, grafana_token, grafana_org_id):
    try:
        tenant_id = sre_spn_credentials['tenant_id']
        client_id = sre_spn_credentials['client_id']
        client_secret = sre_spn_credentials['client_secret']

        azure_keyvault_sre = azure_vars['azure_keyvault_sre']
        azure_keyvault_pattern = azure_vars['azure_keyvault_pattern']

        credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
        secret_client = SecretClient(vault_url=azure_keyvault_sre, credential=credential)
        azure_secret_name = azure_keyvault_pattern + str(grafana_org_id)
        azure_secret_value = grafana_token
        create_azure_secret = secret_client.set_secret(azure_secret_name, azure_secret_value)

        return azure_secret_name, create_azure_secret.id, azure_secret_value
    except Exception as e:
        print(f"An error occurred: {e}")

""" Get Grafana secret stored on the KeyVault """
def get_grafana_secrets(sre_spn_credentials, azure_vars, grafana_org_id):
    try:
        tenant_id = sre_spn_credentials['tenant_id']
        client_id = sre_spn_credentials['client_id']
        client_secret = sre_spn_credentials['client_secret']

        azure_keyvault_sre = azure_vars['azure_keyvault_sre']
        azure_keyvault_pattern = azure_vars['azure_keyvault_pattern']

        credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
        secret_client = SecretClient(vault_url=azure_keyvault_sre, credential=credential)
        grafana_secret_name = azure_keyvault_pattern + str(grafana_org_id)
        secret = secret_client.get_secret(grafana_secret_name)

        return secret.name,secret.id,secret.value
    except Exception as e:
        print(f"An error occurred: {e}")