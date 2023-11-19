import openstack

def list_instances(conn):
    instances = conn.compute.servers()
    print("Available instances:")
    print('')
    for instance in instances:
        print(f"ID: {instance.id}, Name: {instance.name}")

def delete_instance(conn, instance_name):
    try:
        instancia = conn.compute.find_server(instance_name)

        if instancia:
            conn.compute.delete_server(instancia, ignore_missing=True)
            print(f"Instance '{instance_name}' deletion success.")
            print('')

            delete_keypair(conn, instance_name)
        else:
            print(f"There is not an instance with that name '{instance_name}'.")
            print('')
    except Exception as e:
        print(f"Error trying to delete the instance: {e}")
        print('')

def delete_keypair(conn, keypair_name):
    try:
        keypair = conn.compute.find_keypair(keypair_name)

        if keypair:
            conn.compute.delete_keypair(keypair)
            print(f"Keypair '{keypair_name}' deletion success.")
            print('')
        else:
            print(f"There is no keypair with the name '{keypair_name}'.")
            print('')
    except Exception as e:
        print(f"Error trying to delete the keypair: {e}")
        print('')

conn = openstack.connect(cloud='openstack')

list_instances(conn)
print('')

instance_name_to_delete = input("Enter the name of the instance to delete: ")
print('')

delete_instance(conn, instance_name_to_delete)