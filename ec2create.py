import boto3

# Create an EC2 client
ec2 = boto3.resource('ec2', region_name='us-east-1')  # Change region if needed

# Launch EC2 instance
instance = ec2.create_instances(
    ImageId="ami-0c55b159cbfafe1f0",  # Amazon Linux 2 AMI (change based on your region)
    InstanceType="t2.micro",
    KeyName="your-key-name",  # Replace with your AWS key pair name
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "MyPythonEC2"}],
        }
    ],
)

# Print instance ID
print(f"EC2 instance created with ID: {instance[0].id}")
