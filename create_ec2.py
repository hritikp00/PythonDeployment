import boto3

#Set up EC2 client
ec2 = boto3.client('ec2')

#Specify instance parameter
image_id = ''
instance_type = 't2.micro'
key_name = 'wordpress'
security_group_ids = ['']
subnet_id = ''

#Launch EC2 instance
response = ec2.run_instances(ImageId=image_id, InstanceType=instance_type, KeyName=key_name ,MaxCount=1)

#Get instance ID from response
instance_id = response['Instances'][0]['InstanceID']

#Wait for instnace to be running
ec2.get_waiter('instance_running').wait(InstanceIds=[instance_id])

#Print instance information
instance = ec2.describe_instances(Instance_IDS=[instance_id])['Reservations'][0]['Instances'][0]
print(f"Instance ID: {instance_id}")
print(f"Public IP address : {instance.get('PublicIpAddress','N/A')}")
print(f"Private IP address : {instance.get('PrivateIpAddress','N/A')}")
