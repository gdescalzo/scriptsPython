import openstack

def list_instances(conn):
    instances = conn.compute.servers()
    print("Available instances:")
    print('')
    for instance in instances:
        print(f"ID: {instance.id}, Name: {instance.name}")

def stop_instance(conn, instance_name):
    try:
        instance = conn.compute.find_server(instance_name)

        if instance:
            conn.compute.stop_server(instance)
            print(f"Instance '{instance_name}' stopped successfully.")
        else:
            print(f"No instance found with the name '{instance_name}'.")
    except Exception as e:
        print(f"Error while trying to stop the instance: {e}")

conn = openstack.connect(cloud='openstack')

list_instances(conn)
print('')

instance_name_to_stop = input("Enter the name of the instance to stop: ")
print('')

stop_instance(conn, instance_name_to_stop)
print('')