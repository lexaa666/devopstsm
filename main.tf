terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
   required_version = ">= 0.14.9"
}
provider "aws" {
  region = var.aws_region
  shared_credentials_file = "~/.aws/credentials"
}

resource "aws_instance" "ec2_instance_ab_pub" {
  ami = "ami-04e601abe3e1a910f"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.ab_publicsubnet.id

  provisioner "local-exec" {
    command = "sudo apt-get install nginx -y"
    }
  tags = {
    Name = "ab_tf_pub"
  }
}

resource "aws_network_interface_sg_attachment" "sg_attachment_pub_ab" {
  network_interface_id = aws_instance.ec2_instance_ab_pub.primary_network_interface_id
  security_group_id    = aws_security_group.allow_http_ssh_pub.id
}


resource "aws_instance" "ec2_instance_ab_priv" {
  ami = "ami-04e601abe3e1a910f"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.ab_privatesubnet.id
  tags = {
    Name = "ab_tf_priv"
  }
}

resource "aws_network_interface_sg_attachment" "sg_attachment_priv_ab" {
  network_interface_id = aws_instance.ec2_instance_ab_priv.primary_network_interface_id
  security_group_id    = aws_security_group.allow_http_ssh_priv.id
}