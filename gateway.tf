resource "aws_internet_gateway" "IGW" {
  vpc_id = aws_vpc.ab_vpc.id
}
resource "aws_eip" "abEIP" {
  vpc = true
}

resource "aws_nat_gateway" "NAT-GW" {
  allocation_id = aws_eip.abEIP.id
  subnet_id     = aws_subnet.ab_publicsubnet.id
}