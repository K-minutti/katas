variable "region" {
  description = "AWS region where the Elasticache Redis cluster will be created."
  type        = string
  default     = "us-east-1"
}

variable "node_type" {
  description = "ElastiCache node type for the Redis cluster."
  type        = string
  default     = "cache.t3.small"
}
