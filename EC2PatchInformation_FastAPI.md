```bash
from fastapi import FastAPI
import boto3
import json
from pprint import pprint
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import FastAPI, Depends, HTTPException, status
import logging

API_TOKEN = "XXXXXX"

#Initialize the FAST API
#app = FastAPI()
security = HTTPBearer()


"""
“Run the security function and give me its result”

FastAPI automatically:

Executes security()
Extracts the token
Passes it into your function

Step 1 → security() reads header
Step 2 → creates credentials object
Step 3 → passes it to verify_token()

""""

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer" or credentials.credentials != API_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API token"
        )

app = FastAPI(dependencies=[Depends(verify_token)])


#logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s", handlers=[sys.stdout])

@app.get("/ec2/instance_metadata",response_class=HTMLResponse)
async def get_ec2_metadata(instance_id: str,account_no: str,region: str):
    ROLE_NAME="ResourceRO"
    target_role_arn = f"arn:aws:iam::{account_no}:role/{ROLE_NAME}"
    sts_client = boto3.client('sts')

    assume_role_object = sts_client.assume_role(
                RoleArn=target_role_arn,
                RoleSessionName="FastAPIEc2InventorySession",
                DurationSeconds=900
                )

    credentials = assume_role_object['Credentials']

    session = boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken'],
            region_name=region
        )


    ec2_client = session.client('ec2')
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    pretty_json_string = json.dumps(response, indent=4, default=str)
    html_content = f"<pre style='font-family: monospace; background-color: #f4f4f4; padding: 20px;'>{pretty_json_string}</pre>"
    return HTMLResponse(content=html_content)


@app.get("/ec2/instance_MissingPatches",response_class=HTMLResponse)
async def get_missing_patches(instance_id: str,account_no: str,region: str):
    ROLE_NAME="ResourceRO"
    target_role_arn = f"arn:aws:iam::{account_no}:role/{ROLE_NAME}"
    print(target_role_arn)
    sts_client = boto3.client('sts')

    missing_patch_list = []
    result = []

    assume_role_object = sts_client.assume_role(
                RoleArn=target_role_arn,
                RoleSessionName="FastAPIEc2InventorySession",
                DurationSeconds=900
                )

    credentials = assume_role_object['Credentials']

    session = boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken'],
            region_name=region
        )
    print(f"The instance id is {instance_id}, account number is {account_no} and region is {region} ")
    ssm = session.client("ssm",region_name=region)
            
    paginator_patches = ssm.get_paginator("describe_instance_patches")

    for patch_page in paginator_patches.paginate(InstanceId=instance_id,Filters=[{"Key": "State", "Values": ["Missing"]}]):
        for patch in patch_page["Patches"]:
            print(patch)
            missing_patch_list.append(patch["Title"])

    result.append({
        "instance_id": instance_id,
        "patches": missing_patch_list  
    })        

    pretty_json_string = json.dumps(result, indent=4, default=str)
    html_content = f"<pre style='font-family: monospace; background-color: #f4f4f4; padding: 20px;'>{pretty_json_string}</pre>"
    return HTMLResponse(content=html_content)



@app.get("/ec2/ManagedInstances")
async def get_Managed_Instances(account_no: str,region: str):
    ROLE_NAME="ResourceRO"
    target_role_arn = f"arn:aws:iam::{account_no}:role/{ROLE_NAME}"
    sts_client = boto3.client('sts')
    instance_ids = []
    

    assume_role_object = sts_client.assume_role(
                RoleArn=target_role_arn,
                RoleSessionName="FastAPIEc2InventorySession",
                DurationSeconds=900
                )

    credentials = assume_role_object['Credentials']

    session = boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken'],
            region_name=region
            )

    ssm_client = session.client("ssm", region_name=region)

    paginator = ssm_client.get_paginator("describe_instance_information")
    print(paginator)
    for page in paginator.paginate():
        for instance in page["InstanceInformationList"]:
            instance_ids.append(instance["InstanceId"])

    return instance_ids   
    
@app.get("/ec2/Managed_Instances_MissingPackages")
async def get_Managed_Instances_MissingPackages(account_no: str,region: str):
    ROLE_NAME="ResourceRO"
    target_role_arn = f"arn:aws:iam::{account_no}:role/{ROLE_NAME}"
    sts_client = boto3.client('sts')
    instance_ids = []
    #missing_patch_list = []
    result = []
    
    assume_role_object = sts_client.assume_role(
                RoleArn=target_role_arn,
                RoleSessionName="FastAPIEc2InventorySession",
                DurationSeconds=900
                )

    credentials = assume_role_object['Credentials']

    session = boto3.Session(
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken'],
            region_name=region
            )

    ssm_client = session.client("ssm", region_name=region)

    paginator = ssm_client.get_paginator("describe_instance_information")
    print(paginator)
    for page in paginator.paginate():
        for instance in page["InstanceInformationList"]:
            
            instance_ids.append(instance["InstanceId"])

    paginator_patches = ssm_client.get_paginator("describe_instance_patches")

    for instance in instance_ids:
        missing_patch_list = [] 
        for patch_page in paginator_patches.paginate(InstanceId=instance,Filters=[{"Key": "State", "Values": ["Missing"]}]):
            print(patch_page)
            for patch in patch_page["Patches"]:
                print(patch)
                missing_patch_list.append(patch["Title"])
        
        result.append({
        "instance_id": instance,
        "patches": missing_patch_list  
        })   
        
    pretty_json_string = json.dumps(result, indent=4, default=str)
    html_content = f"<pre style='font-family: monospace; background-color: #f4f4f4; padding: 20px;'>{pretty_json_string}</pre>"
    return HTMLResponse(content=html_content)
```
