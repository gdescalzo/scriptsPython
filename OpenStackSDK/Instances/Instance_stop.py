import openstack

def list_instances(conn):
    instances = conn.compute.servers()
    print("Available instances:")
    for instance in instances:
        print(f"ID: {instance.id}, Name: {instance.name}")

def stop_instance(conn, instance_name):
    try:
        # Get information about the instance by name
        instance = conn.compute.find_server(instance_name)

        # Check if the instance exists
        if instance:
            # Stop the instance
            conn.compute.stop_server(instance)
            print(f"Instance '{instance_name}' stopped successfully.")
        else:
            print(f"No instance found with the name '{instance_name}'.")
    except Exception as e:
        print(f"Error while trying to stop the instance: {e}")

# Initialize the connection
conn = openstack.connect(cloud='openstack')

# List and select an instance to stop
list_instances(conn)
instance_name_to_stop = input("Enter the name of the instance to stop: ")

# Stop the selected instance
stop_instance(conn, instance_name_to_stop)