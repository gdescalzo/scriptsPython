sre_spn_credentials = {
    "tenant_id" : "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
    "client_id" : "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",
    "client_secret" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

azure_vars = {
    "azure_keyvault_pattern" : "BigMonitor-TokenOrg-",
    "azure_keyvault_grafana_user" : "BigMonitor-Admin-User",
    "azure_keyvault_grafana_password" : "BigMonitor-Admin-Password",
    "azure_keyvault_sre": "https://xxxxxxxxx.vault.azure.net/"
}

grafana_vars = {
    "grafana_org_token_role" : "Admin",
    "grafana_fqdn" : "https://bigmonitor.sbp.eyclienthub.com",
    "grafana_endpoint_create_org" : "/api/orgs",
    "grafana_endpoint_create_token" : "/api/auth/keys",
    "grafana_endpoint_get_folder" : "/api/folders",
    "grafana_endpoint_create_folder" : "/api/folders",
    "grafana_endpoint_create_datasource" : "/api/datasources",
    "grafana_endpoint_adduser" : "/api/org/users"
}

sre_user_list = [
    'some@email.com',
    'some1@email.com'
]




