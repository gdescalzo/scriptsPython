import openstack

def list_flavors(conn):
    flavors = conn.compute.flavors()
    print("Available flavors:")
    print('')
    for flavor in flavors:
        print(f"ID: {flavor.id}, Name: {flavor.name}")

# Initialize the connection
conn = openstack.connect(cloud='openstack')
        
# List and select a flavor
list_flavors(conn)
print('')