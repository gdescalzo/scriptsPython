import openstack

def list_instances(conn):
    instances = conn.compute.servers()
    print("Available instances:")
    for instance in instances:
        print(f"ID: {instance.id}, Name: {instance.name}")

def delete_instance(conn, instance_name):
    try:
        instancia = conn.compute.find_server(instance_name)
        if instancia:
            conn.compute.delete_server(instancia, ignore_missing=True)
            print(f"Instance '{instance_name}' deletion success.")
        else:
            print(f"There is not an instance with that name '{instance_name}'.")
    except Exception as e:
        print(f"Error trying to delete the instance: {e}")

# Initialize the connection
conn = openstack.connect(cloud='openstack')

# List and select an instance to delete
list_instances(conn)
instance_name_to_delete = input("Enter the name of the instance to delete: ")

# Delete the selected instance
delete_instance(conn, instance_name_to_delete)