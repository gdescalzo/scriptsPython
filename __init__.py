""" Import Module / method """
from moduleAzure import get_grafana_credentials, store_grafana_token, get_grafana_secrets
from moduleGrafana import create_grafana_org, create_grafana_token, get_grafana_org_folders, create_grafana_org_folders, create_grafana_datasource #, add_grafana_sre_users
import moduleCredentials

""" Var Inputs """
grafana_org_name = input("Please input an Grafana organization name: ")
grafana_org_app_folder_name = input("Please input an Grafana folder name for your application: ")
azure_subscription_id = input("Please input an Azure Subscription Id for the Data Source creation: ")

""" Var Inports """
sre_spn_credentials = moduleCredentials.sre_spn_credentials
azure_vars = moduleCredentials.azure_vars
grafana_vars = moduleCredentials.grafana_vars
#sre_user_list = moduleCredentials.sre_user_list

""" Get Grafana admin credentials stored in Azure KeyVaul """
grafana_user, grafana_password = get_grafana_credentials(sre_spn_credentials, azure_vars)
""" Testing output """
print()
print("Grafana admin user: ", grafana_user)
print("Grafana admin password", grafana_password)
print()

""" Create Grafana organization """
grafana_org_output_message, grafana_org_id= create_grafana_org(grafana_vars, grafana_org_name, grafana_user, grafana_password)
""" Testing output """
print("Grafana Org create message response: ", grafana_org_output_message)
print("Grafana Org create id response: ", grafana_org_id)
print()

""" Create Grafana token organization """
grafana_token = create_grafana_token(grafana_vars, grafana_user, grafana_password, grafana_org_name, grafana_org_id)
""" Testing output """
print("Print Grafana Token created: ", grafana_token)
print()


""" Store Grafana Token in Azure KeyVaul """
grafana_secret_name, grafana_secret_id, grafana_secret_value = store_grafana_token(sre_spn_credentials, azure_vars, grafana_token, grafana_org_id)
""" Testing output """
print("Store Grafana Token Name: ", grafana_secret_name)
print("Store Grafana Token ID: ", grafana_secret_id)
print("Store Grafana Token Value: ", grafana_secret_value)
print()


""" Get Grafana Token in Azure KeyVaul """
grafana_keyvault_secret_name, grafana_keyvault_secret_id, grafana_keyvault_secret_value = get_grafana_secrets(sre_spn_credentials, azure_vars, grafana_org_id)
""" Testing output """
print("Get Grafana Token in Azure KeyVaul secret name: ", grafana_keyvault_secret_name)
print("Get Grafana Token in Azure KeyVaul secret id: ", grafana_keyvault_secret_id)
print("Get Grafana Token in Azure KeyVaul secret value: ", grafana_keyvault_secret_value)


""" Create Grafana Folder """
create_grafana_org_folders_output = create_grafana_org_folders(grafana_vars, grafana_org_app_folder_name, grafana_keyvault_secret_value)
""" Testing output """
print()
print("Output of create folder: ", create_grafana_org_folders_output)


""" Get Grafana Folder list """
grafana_org_folders_list = get_grafana_org_folders(grafana_vars, grafana_keyvault_secret_value)
print()
""" Testing output """
print("List of folders: ", grafana_org_folders_list)


""" Create Grafana Data Source """
grafana_data_source = create_grafana_datasource(sre_spn_credentials, grafana_vars, grafana_org_name, grafana_org_id, grafana_keyvault_secret_value, azure_subscription_id, grafana_org_app_folder_name)
""" Testing output """
print()
print("Output of create Data Source: ", grafana_data_source)


""" Add Grafana SRE users 
add_grafana_sre_users(grafana_vars, sre_user_list, grafana_keyvault_secret_value)
"""