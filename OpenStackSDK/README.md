# OpenStackSDK

## Introduction

> This repository contains information related to the OpenStackSDK, primarily focusing on listing, modifying, creating, and deleting resources within your OpenStack environment using the SDK interface.

> To interact with the OpenStack platform through this SDK, certain requirements must be met to ensure access to the OpenStack environment. The interaction process is outlined as follows:

> As depicted in the image, OpenStack exposes various services that can be accessed externally through the SDK. It establishes an HTTPS tunnel to communicate with different endpoints, facilitating the retrieval of responses.

## Objective

> Testing OpenStack functionalities using the Python library. Establishing connectivity with Horizon and other OpenStack components through the SDK.


## Pre-Requisits

> To ensure everything works seamlessly, you need to prepare your environment based on your platform, taking into account the following considerations:

<details>
<summary>SDK Requisits (click para expandir)</summary>

> Required software

> In my case, when testing all these functionalities, I had to perform the tasks on Windows. However, the requirements may vary for you, depending on your operating system.

- Install [Python](https://www.python.org/downloads/)
- Upgrade [pip](https://www.wikihow.com/Update-Pip)
- Install [Microsoft Visual C++](https://learn.microsoft.com/es-es/cpp/windows/latest-supported-vc-redist?view=msvc-170)
- Install [OpenStack SDK](https://docs.openstack.org/openstacksdk/latest/install/index.html)

> Configuration

1. Create "Connection Object"
2. Specify the service type that you have to query
3. Specify the resource type that you have to query
4. Specify the version of the component that you want to modify, create, delete or list.

</details>
