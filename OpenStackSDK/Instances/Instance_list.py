import openstack

def list_instances(conn):
    instances = conn.compute.servers()
    print("Available instances:")
    for instance in instances:
        print(f"ID: {instance.id}, Name: {instance.name}")

# Initialize the connection
conn = openstack.connect(cloud='openstack')

# List and select an instance to delete
list_instances(conn)