# Azure Alerts Export Script

## Description

> The Azure Alerts Export Script is designed to fetch Azure Monitor Alert data from both Metric Alerts and Log Analytics Alerts through the Azure Management API. The fetched data is processed and converted into a readable format (pandas DataFrame), and exported into an Excel file.
>
> There is two ways to use this solution, one **Local** (_on you PC_) or **Remote** (_by using GitHub Actions through a pipeline execution, and then downloading the artifact_).

<hr>

## Core Functions

### get_metric_alerts()

> This function is designed to fetch the data from Azure Metric Alerts. It uses the Azure Management API to fetch the data, which is then returned as a pandas DataFrame.

### get_log_query_alerts()

> Similar to `get_metric_alerts()`, this function fetches data, but from Azure Log Query Alerts. The resulting data is also returned as a pandas DataFrame.

### Data Processing and Output

> After fetching, the data is processed for any missing values in the "Alert Evaluation Frequency" and "Alert Window Size" columns. Any missing values are correctly handled.
>
> The data is then exported as an Excel file, with the filename as `'Some Name'` followed by the current date for easy identification.

<hr>

## Local Execution

> This guide provides instructions for executing the script on your personal computer. 

### Usage Guide

1. Clone the Repository

   > Use the following command to clone the repository:
   >
   > ``git clone <repository-link>``

<br />

2. Navigate to the Directory

   > Once cloned, navigate to the directory containing the script:
   >
   > ``cd <repository-folder>``

<br />

3. Install Required Packages

   > Before running the script, necessary Python libraries must be installed. These include the Azure SDK for Python, pandas, and openpyxl. Use the following command to install them:
   >
   > ``pip install -r requirements.txt``
   >
   > The Script requires the following Python packages:
   >
   > - Azure SDK for Python (azure-mgmt-monitor and azure-identity)
   > - xlwt
   > - pandas
   > - datetime
   > - openpyxl
   > - azure.identity
   > - azure.mgmt.monitor 
   > - azure.mgmt.subscription 

<br />

4. To ensure the successful operation of the script, it's mandatory to modify the `SRE_Credential.JSON` file. This file is used to authenticate with Azure, hence it should be updated with your accurate Azure login details.

   > | Note | _Please ensure that you have the necessary permissions on your Azure account to fetch alert data. If any issues occur during fetching, please verify your account permissions._ |
   > | - | - |
   >
   >```
   >{
   >    "sre_credentials": [
   >        {
   >            "tenant_id" : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   >            "client_id" : "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
   >            "client_secret" : "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
   >        }
   >    ]
   >}
   >```

<br />

6. Configure the running path. Yo need to change for your right path.

   > ``filepath = r'C:\Users\RE834YF\OneDrive - EY\Documents\EY\Scripts\Azure\Azure Alerts\Python\SRE_Credentials.json'``

<br />

5. Running the Script

   > To run the script, use:
   >
   > ``python <script-name.py>``
   >
   > On first run, you will be asked to provide Azure credentials. These credentials are stored as environment variables, and will automatically be used in any subsequent script execution.
   >

<hr>

## Remote Execution (_via GitHub Actions_)

> As mentioned earlier, GitHub provides an alternate way to run this script using GitHub Actions. You can execute the script directly from GitHub by triggering the `Run Azure Alerts Export Script` pipeline as needed. This is an advantageous option for those who wish to automate execution without running the script locally on their computers.

### Usage Guide

1. Configure Secrets
    For remote execution, you'll need to store your Azure credentials as secrets in your GitHub repository to allow the script to authenticate with Azure.
    - Go to your GitHub repository, navigate to `Settings > Secrets` and edit the current secrets, right now are set the SPN of the SRE team, but if for some reason you want to change that, the mentioned explanation is the way.

2. Running the GitHub Action
    Once the secrets, you can trigger your workflow manually from the `Actions` tab in your GitHub repository, or it will run automatically based on your `azure_alerts.yml` configuration.

3. Access the Output
    The pipeline is configured to generate an artifact which is your output Excel file. At the end of the workflow run, it can be downloaded from `Actions > Your workflow run > Artifacts`.

