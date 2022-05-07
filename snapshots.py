import boto3

ec2 = boto3.resource('ec2',region_name = 'us-west-2')
snapshot_id_list = []

backup_filters = [

        {
  'Name': 'tag:Backup',
  'Values': ['Yes']
        }
]

for instances in ec2.instances.filter(Filters=backup_filters):
    for volume in instances.volumes.all():
        snapshot = volume.create_snapshot(Description='Created using boto3')
        snapshot_id_list.append(snapshot.snapshot_id)
        print('The EC2 instnace is {} and snapshot id {}'.format(instances.instance_id,snapshot.snapshot_id))


for snaps in snapshot_id_list:
    print (snaps)
