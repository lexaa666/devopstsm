resource "aws_route_table" "privRT" {
  vpc_id = aws_vpc.ab_vpc.id
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.NAT-GW.id
  }
}

resource "aws_route_table" "publRT" {
  vpc_id = aws_vpc.ab_vpc.id
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = aws_nat_gateway.NAT-GW.id
  }
}

resource "aws_route_table_association" "PubRTAss" {
  route_table_id = aws_route_table.publRT.id
  subnet_id      = aws_subnet.ab_publicsubnet.id
}

resource "aws_route_table_association" "PrivRTAss" {
  route_table_id = aws_route_table.privRT.id
  subnet_id      = aws_subnet.ab_privatesubnet.id
}