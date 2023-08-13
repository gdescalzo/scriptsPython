import requests
import json

url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

response = requests.get(url)
parsed_data = json.loads(response.content)

for item in parsed_data:
    casa_info = item["casa"]
    if casa_info["nombre"] == "Dolar Blue":
        nombre = casa_info["nombre"]
        compra = casa_info["compra"]
        venta = casa_info["venta"]

        print(f"Nombre: {nombre}\nCompra: {compra}\nVenta: {venta}\n")