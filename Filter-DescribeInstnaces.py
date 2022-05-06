import boto3
import json
ec2_client = boto3.client('ec2',region_name='us-west-2')

# Filters are the list either we can use 1 filter or multiple filter
#values are also list
resp = ec2_client.describe_instances(
        Filters=[{'Name':'instance-state-name','Values': ['running']},{'Name': 'instance-type', 'Values': ['t2.micro']}])


#print (json.dumps(resp, indent=2, default=str))

for reservation  in resp['Reservations']:
    for instance in reservation['Instances']:
        print ("Instnace is {}".format(instance['InstanceId']))
        print ("PrivateDnsName is {}".format(instance['PrivateDnsName']))
