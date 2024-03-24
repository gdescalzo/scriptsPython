import requests

# URL del servicio de identidad de OpenStack (Keystone)
identity_url = 'SomeURL'

# Credenciales de autenticación
username = 'SomeUser'
password = 'SomePassword'
project_name = 'SomeProjectName'

# Construir la solicitud de autenticación
auth_data = {
    'auth': {
        'identity': {
            'methods': ['password'],
            'password': {
                'user': {
                    'name': username,
                    'domain': {'id': 'default'},
                    'password': password
                }
            }
        },
        'scope': {
            'project': {
                'name': project_name,
                'domain': {'id': 'default'}
            }
        }
    }
}

headers = {'Content-Type': 'application/json'}

# Realizar la solicitud de autenticación
response = requests.post(identity_url, json=auth_data, headers=headers)

# Verificar si la autenticación fue exitosa
if response.status_code == 201:
    # Extraer el token del encabezado de respuesta
    x_auth_token = response.headers['X-Subject-Token']
    print(f'Token de autenticación obtenido: {x_auth_token}')
else:
    print(f'Error en la autenticación: {response.status_code} - {response.text}')
