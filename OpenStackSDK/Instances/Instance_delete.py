import openstack

conn = openstack.connect(cloud='openstack')

instance_name = 'test1'

try:
    instancia = conn.compute.find_server(instance_name)
    if instancia:
        conn.compute.delete_server(instancia, ignore_missing=True)
        print(f"Instance '{instance_name}' deletion success.")
    else:
        print(f"There is not an instance with that name '{instance_name}'.")
        
except Exception as e:
    print(f"Error trying to delete the instance: {e}") 