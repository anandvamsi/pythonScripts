import boto3
client = boto3.resource('ec2',region_name='us-west-2')

for instances in client.instances.filter(Filters=[
    {
      'Name': 'availability-zone',
      'Values': ['us-west-2a']
     }

]):
    print ('The instance is {} and instances type is {}'.format(instances.instance_id,instances.instance_type))
