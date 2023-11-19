import openstack

def list_instances(conn):
    instances = conn.compute.servers()
    print("Available instances:")
    print('')
    for instance in instances:
        print(f"ID: {instance.id}, Name: {instance.name}")

conn = openstack.connect(cloud='openstack')

list_instances(conn)
print('')