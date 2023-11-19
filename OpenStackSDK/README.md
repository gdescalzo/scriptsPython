# OpenStackSDK

## Introduction

> This repository contains information related to the OpenStackSDK, primarily focusing on listing, modifying, creating, and deleting resources within your OpenStack environment using the SDK interface.

- Module: **Instances**

## Objective

> Testing OpenStack functionalities using the Python library. Establishing connectivity with Horizon and other OpenStack components through the SDK.

## Pre-Requisites

> To ensure everything works seamlessly, you need to prepare your environment based on your platform, taking into account the following considerations:

- To interact with the OpenStack platform through this SDK, certain requirements must be met to ensure access to the OpenStack environment. The interaction process is outlined as follows.

> As depicted in the image, OpenStack exposes various services that can be accessed externally through the SDK. It establishes an HTTPS tunnel to communicate with different endpoints, facilitating the retrieval of responses.

<details>
<summary>SDK Requisites (click to expand)</summary>

### Software required

> In my case of study I made all test over Windows platform

- Install [Python](https://www.python.org/downloads/)
- Upgrade [pip](https://www.wikihow.com/Update-Pip)
- Install [Microsoft Visual C++](https://learn.microsoft.com/es-es/cpp/windows/latest-supported-vc-redist?view=msvc-170)
- Install [OpenStack SDK](https://docs.openstack.org/openstacksdk/latest/install/index.html)

</details>

<details>
<summary>SDK Configuration (click to expand)</summary>

> To use the SDK you should have the configure:

1. Create "Connection Object"
2. Specify the service type that you have to query
3. Specify the resource type that you have to query
4. Specify the version of the component that you want to modify, create, delete or list.

### Object Connection

> There is two ways based o the OpenStack Official documentation to create a [Connection Object](https://docs.openstack.org/openstacksdk/latest/user/connection.html#openstack.connection.Connection).

> There is 3 ways to create a connection object (_here the [Link](https://docs.openstack.org/openstacksdk/latest/user/guides/connect.html) of the official documentation_) but the most re comended one is through [Config Files](https://docs.openstack.org/openstacksdk/latest/user/config/configuration.html#config-clouds-yaml). For the testing case that you can see on this repo I used the **Config Files**

```
# Example of creating a connection object using Config Files
import openstack

# Load connection configuration from the config file
conn = openstack.connect(cloud='mycloud')
```

### Specify the service type

> Specify the type of service you need to query within the OpenStack environment.

```
# Example of specifying the service type
service_type = 'compute'
```

### Specify the resource type

> Specify the type of resource you want to interact with within the OpenStack environment.

```
# Example of specifying the resource type
resource_type = 'servers'
```

### Specify the version

> Specify the version of the OpenStack component you want to modify, create, delete, or list.

```
# Example of specifying the version of the component
component_version = 'v2.1'
```

</details>

## Sources documents

- [Getting Started with OpenStack Python SDK](https://www.sebae.net/videos/getting-started-with-openstack-python-sdk-2/)
- [Connecting to openstack using openstacksdk in python](https://www.youtube.com/watch?v=ApEPfhKmVWE)
- [OpenStack Connect](https://docs.openstack.org/openstacksdk/latest/user/guides/connect.html)
- [Configuring OpenStack SDK Applications](https://docs.openstack.org/openstacksdk/latest/user/config/configuration.html)
