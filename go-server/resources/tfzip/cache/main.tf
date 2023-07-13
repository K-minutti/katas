provider "aws" {
  region = var.region
}

resource "aws_elasticache_subnet_group" "example" {
  name       = "example-subnet-group"
  subnet_ids = ["subnet-12345678", "subnet-abcdefgh"]  # Replace with your subnet IDs
}

resource "aws_elasticache_parameter_group" "example" {
  name   = "example-parameter-group"
  family = "redis6.x"

  parameter {
    name  = "activerehashing"
    value = "yes"
  }

  parameter {
    name  = "maxmemory-policy"
    value = "allkeys-lru"
  }
}

resource "aws_elasticache_replication_group" "example" {
  replication_group_id        = "example-redis-cluster"
  replication_group_description = "Example Redis Cluster"

  node_type                   = var.node_type
  port                        = 6379
  automatic_failover_enabled  = true
  num_cache_clusters          = 2
  engine_version              = "6.x"
  parameter_group_name        = aws_elasticache_parameter_group.example.name
  subnet_group_name           = aws_elasticache_subnet_group.example.name

  cluster_mode {
    replicas_per_node_group = 1
    num_node_groups         = 2
  }

  tags = {
    Name = "example-redis-cluster"
  }
}
