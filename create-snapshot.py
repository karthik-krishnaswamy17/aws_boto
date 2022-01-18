from operator import eq
import boto3
ec2_c = boto3.client('ec2', region_name='ap-south-1')
ec2_r = boto3.resource('ec2', region_name='ap-south-1')

#List all volumes for given AWS account.
volumes=ec2_c.describe_volumes()['Volumes']

# volume_list= { volume['VolumeId']:volume['State'] for volume in volumes  }
def create_snaphot():
    for volume in volumes:
        if volume['State'] == 'in-use':
            vol_id=volume['VolumeId']
            volume_resource= ec2_r.Volume(vol_id)
            # snapshot = ec2_r.Snapshot(vol_id)
            volume_resource.create_snapshot()
            print(f"{vol_id}:: Snaphot initiated...")
        else:
            print(f"{volume['VolumeId']}:: Cannot create snapshot.Volume not been used.")



create_snaphot()