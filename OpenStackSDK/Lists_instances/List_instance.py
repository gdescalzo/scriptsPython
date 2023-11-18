import openstack

# Initialize connection
conn = openstack.connect(cloud='openstack')

for server in conn.compute.servers():
    print(server.to_dict())
