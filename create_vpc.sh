#!/bin/bash

#Task1
echo "Create VPC"
VPC_ID=`aws ec2 create-vpc --cidr-block 10.0.0.0/16  --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=AlekseyBirulya}]' --query Vpc.VpcId --output text`
echo "VPC Success: $VPC_ID"
echo "Create Subnet"
SUBNET_ID=`aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.1.0/24 --availability-zone eu-central-1a --query Subnet.SubnetId --output text`
echo "Subnet Success: $SUBNET_ID"
echo "Create Gatway"
GETWAY_ID=`aws ec2 create-internet-gateway --query InternetGateway.InternetGatewayId --output text`
echo "Getway Success: $GETWAY"
echo "Connect Getway to VPC"
aws ec2 attach-internet-gateway --vpc-id $VPC_ID --internet-gateway-id $GETWAY_ID
echo "Connect Success"
echo "Create Route-Table"
ROUTE_TABLE_ID=`aws ec2 create-route-table --vpc-id $VPC_ID --query RouteTable.RouteTableId --output text`
echo "Route-Table Success"
echo "Connect Route-Table to Getway"
aws ec2 create-route --route-table-id $ROUTE_TABLE_ID --destination-cidr-block 0.0.0.0/0 --gateway-id $GETWAY_ID
echo "Connect Success"
echo "Create Associate-Route-Table"
aws ec2 associate-route-table --route-table-id $ROUTE_TABLE_ID --subnet-id $SUBNET_ID
echo "Associate-Route-Table Success"

###Task3
echo "Create SG"
SG_ID=`aws ec2 create-security-group --group-name sg_ab  --description "SG_AlekseyBirulya" --vpc-id $VPC_ID --output text`
echo "SG Success"
echo "Add port 22 SG"
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 22 --cidr 0.0.0.0/0
echo "Port 22  Success"
echo "Add port 8080 SG"
aws ec2 authorize-security-group-ingress --group-id $SG_ID --protocol tcp --port 8080 --cidr 0.0.0.0/0
echo "Port 8080 Success"

#Task2
echo "Create Instance Ubuntu t2.micro"
aws ec2 run-instances --image-id ami-0ab1a82de7ca5889c --count 1 --instance-type t2.micro --key-name my-key-pair --security-group-ids $SG_ID --subnet-id $SUBNET_ID
echo "Instance Success"
