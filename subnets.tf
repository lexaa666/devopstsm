resource "aws_subnet" "ab_publicsubnet" {
  vpc_id     = aws_vpc.ab_vpc.id
  cidr_block = var.pubsubcidr
}
