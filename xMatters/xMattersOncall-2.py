import requests
import json

base_URL = "https://xxxxxxxxxxxxxxxx.xmatters.com/api/xm/1"
endpoint_URL = "/oauth2/token"

client_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
username = "x-api-key-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
password = "xxxxxxxxxxxxxxxxxxxxxxxx"
grant_type = "password"
url = (
    base_URL
    + endpoint_URL
    + "?grant_type="
    + grant_type
    + "&client_id="
    + client_id
    + "&username="
    + username
    + "&password="
    + password
)

headers = {"Content-Type": "application/json"}

response = requests.post(url, headers=headers)

if response.status_code == 200:
    rjson = response.json()
    print(
        "Access token: "
        + rjson.get("access_token")
        + ", \nRefresh token: "
        + rjson.get("refresh_token")
    )
else:
    print("Could not get an access token")   