import openstack

# Initialize the connection
conn = openstack.connect(cloud='openstack')

# Name of the instance you want to stop
instance_name = 'test1'

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
