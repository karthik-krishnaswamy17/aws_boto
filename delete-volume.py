from operator import eq
import boto3
ec2_c = boto3.client('ec2', region_name='ap-south-1')
ec2_r = boto3.resource('ec2', region_name='ap-south-1')

#List all volumes for given AWS account.
volumes=ec2_c.describe_volumes()['Volumes']

# volume_list= { volume['VolumeId']:volume['State'] for volume in volumes  }
def delete_volume():
    for volume in volumes:
        if volume['State'] != 'in-use':
            vol_id=volume['VolumeId']
            volume_resource= ec2_r.Volume(vol_id)
            # print(volume_resource)
            print(f"{vol_id}:: Deleting Volume.")
            volume_resource.delete()
            print(f"{vol_id}:: Deleted Volume successfully.")
        else:
            print(f"{volume['VolumeId']}:: Cannot delete the volume since it's been used.")

delete_volume()