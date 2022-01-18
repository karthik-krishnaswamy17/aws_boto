from operator import eq
import boto3
ec2_c = boto3.client('ec2', region_name='ap-south-1')
ec2_r = boto3.resource('ec2', region_name='ap-south-1')

#List all volumes for given AWS account.
volumes=ec2_c.describe_volumes()['Volumes']

# volume_list= { volume['VolumeId']:volume['State'] for volume in volumes  }
def add_tags():
    for volume in volumes:
        if volume['State'] == 'in-use':
            vol_id=volume['VolumeId']
            volume_resource= ec2_r.Volume(vol_id)
            # print(volume_resource)
            print(f"Creating tags for {vol_id}.")
            volume_resource.create_tags(
                Tags=[
                    {
                     'Key':'Name','Value':'Production-ap'
                    },
                ]
            )
            print(f"Created tags successfully for {vol_id}.")
            print("\n")
        else:
            print(f"Cannot create tags for {volume['VolumeId']} since the volume is not attached.")

add_tags()