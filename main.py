import boto3
import sys
import schedule

try:
    ec2=boto3.client('ec2',region_name='ap-south-1')

    def jobs():
        vpc_state()
        print("\n")
        subnet_state()
        print("\n")
        instance_status()
        print(25*"#")

    def vpc_state():
        vpcs=ec2.describe_vpcs()['Vpcs']
        print(24*"____")
        print("VPC-Id",3*'\t',"Default",1*'\t',"STATE",2*'\t',"CidrBlock")
        print(24*"____")
        for vpc in vpcs:
            print(f"{vpc['VpcId']}\t{vpc['IsDefault']}\t\t{vpc['State']}\t{vpc['CidrBlock']}")
        
    def subnet_state():
        subnets=ec2.describe_subnets()['Subnets']
        # print(24*"____")
        print("AZS",2*'\t',"SUBNET",3*'\t',"STATE",2*'\t',"CIDR",2*'\t',"Avail IP's")
        print(24*"____")
        for s in subnets:
            print(f"{s['AvailabilityZone']}\t{s['SubnetId']}\t{s['State']}\t{s['CidrBlock']}\t\t{s['AvailableIpAddressCount']}")
   
    def instance_status():
        instances=ec2.describe_instance_status(
            IncludeAllInstances=True
                )['InstanceStatuses']
        print(f"Total instance is :{len(instances)}\n")
        for instance in instances:
            print(f"{instance['InstanceId']} is {instance['InstanceState']['Name']} state. System Status: {instance['SystemStatus']['Status']}")
            
    schedule.every(5).seconds.do(jobs)
    while True:
        schedule.run_pending()

   
except:
     print(sys.exc_info())
