import openstack

def list_flavors(conn):
    flavors = conn.compute.flavors()
    print("Available flavors:")
    print('')
    for flavor in flavors:
        print(f"ID: {flavor.id}, Name: {flavor.name}")

def list_images(conn):
    images = conn.compute.images()
    print("Available images:")
    print('')
    for image in images:
        print(f"ID: {image.id}, Name: {image.name}")

def list_networks(conn):
    networks = conn.network.networks()
    print("Available networks:")
    print('')
    for network in networks:
        print(f"ID: {network.id}, Name: {network.name}")

def create_keypair(conn, keypair_name):
    print(f"Creating keypair '{keypair_name}'...")
    print('')
    keypair = conn.compute.create_keypair(name=keypair_name)
    print("Keypair created successfully.")
    print('')
    return keypair

def create_instance(conn, instance_name, flavor_name, image_id, keypair_name):
    try:
        print(f"Creating instance '{instance_name}'...")
        print('')
        # Get the flavor ID based on the flavor name
        flavor = conn.compute.find_flavor(flavor_name)
        if flavor is None:
            raise Exception(f"Flavor '{flavor_name}' not found.")
        flavor_ref = flavor.id

        # List and select a network
        list_networks(conn)
        network_id = input("Enter the ID of the network to use: ")
        print('')

        # Create the instance
        instance = conn.compute.create_server(
            name=instance_name,
            flavorRef=flavor_ref,
            imageRef=image_id,
            key_name=keypair_name,
            networks=[{"uuid": network_id}]  # Specify the network for the instance
        )

        # Wait for the instance to be active
        conn.compute.wait_for_server(instance)

        print(f"Instance '{instance_name}' created successfully.")
    except Exception as e:
        print(f"Error while trying to create the instance: {e}")

# Initialize the connection
conn = openstack.connect(cloud='openstack')

# List and select a flavor
list_flavors(conn)
print('')
flavor_id = input("Enter the ID of the flavor to use: ")

# List and select an image
list_images(conn)
print('')
image_id = input("Enter the ID of the image to use: ")

# Enter the instance name
print('')
instance_name = input("Enter the name for the new instance: ")

# Create keypair with the same name as the instance
keypair_name = instance_name
keypair = create_keypair(conn, keypair_name)

# Create the instance
create_instance(conn, instance_name, flavor_id, image_id, keypair_name)