# AWS teardown inventory

Every AWS resource belonging to this project, with its monthly cost and a
recommendation. Nothing here is deleted automatically. Each item needs
explicit approval, and Imran performs or approves the deletion.

Account 073924410975, region us-east-1. Costs are projected full-month,
pre-tax USD, from the August 2026 bill (29 days observed, scaled to 31).
Add roughly 20% tax on top, which is the ratio seen on the July invoice.

## The short version

The entire bill collapses to $0.08 by deleting one thing. Everything else in
this list is free, or belongs to another project.

## Delete

| Resource | Monthly | Notes |
|---|---:|---|
| ECS Express service `debate-chatbot-8051` in cluster `default` | $35.31 | Fargate 1 vCPU + 2 GB running continuously. Deleting the Express service also removes the load balancer and the addresses below, so this one deletion accounts for $76.45 of the $76.54. Do it only after 48 hours of parallel running and after the custom subdomain points at Cloud Run. |
| ALB `ecs-express-gateway-alb` (6 AZs, internet-facing) | $16.10 | 669 ALB-hours at $0.0225. Actual traffic was 0.798 LCU-hours, one cent. Removed with the Express service; verify it is gone rather than assuming. |
| ~7 public IPv4 addresses | $25.05 | 4,686 address-hours at $0.005. Six ALB nodes, one per availability zone, plus the task ENI. This is the single largest line and none of it is compute. Removed with the ALB. |
| Log group `/aws/ecs/default/debate-chatbot-fc8e-3aea` | $0.00 | Orphaned from an earlier ECS service that no longer exists. |
| Log groups `/aws/apprunner/debate-chatbot/76ec4dc1...` (two) | $0.00 | App Runner was retired in July. Dead logs. |
| CloudWatch alarms: `RollbackAlarm`, `TargetTracking...AlarmLow`, `TargetTracking...AlarmHigh` | $0.00 | All three are auto-created by the Express service and its autoscaling. They go with it. AlarmLow sitting in ALARM is normal: it means "scale down", not a fault. |

## Keep, deliberately

| Resource | Monthly | Why |
|---|---:|---|
| ECR repository `churn-api` | ~$0.00 | **Different project.** Do not touch. |
| Log group `/aws/apprunner/churn-api-prod/1acc6d76...` | $0.00 | Same. Different project. |
| ECR repository `debate-chatbot` and its images | $0.08 | Keep for about a month as a rollback path, then delete. 0.767 GB at $0.10/GB-month. |
| Log group `/aws/ecs/default/debate-chatbot-8051-0d41` | $0.00 | Keep 30 days in case something surfaces after cutover. Set a retention policy: it is currently "Never expire", like every log group in this account. |
| Task definitions, `debate-chatbot` family | $0.00 | Free to keep, and they are the record of the AWS work. Worth more on a CV than the running service. |
| ECS cluster `default` | $0.00 | An empty cluster costs nothing and this is the account default. |
| IAM role `ecsTaskExecutionRole` | $0.00 | Free, shared, needed by any future ECS work. |
| IAM role `ecsInfrastructureRoleForExpressServices` | $0.00 | Free. Worth keeping specifically because it is awkward to recreate: as the README notes, the CLI cannot create it and you have to go through the Console Express flow to get it back. |
| VPC `vpc-0fcf3826099d08c88` | $0.00 | The account's default VPC, not something this project created. Leave it. |

## Not present

- **No NAT Gateway.** The brief expected one. There isn't one, and there never
  was: the $26 VPC line is entirely public IPv4 address rent. Worth saying out
  loud because a NAT Gateway is the usual suspect for a VPC line item this
  size, and the real answer here is more interesting.
- **No VPC endpoints.**
- **No Elastic IPs** held separately from the ALB.
- **Data transfer: $0.00.** Traffic is too low to leave the free tier.

## Order of operations

1. Cloud Run deployed and verified (parity harness green).
2. Custom subdomain pointing at Cloud Run, propagated.
3. Both deployments running in parallel for at least 48 hours.
4. Delete the ECS Express service. Confirm the ALB and the IPv4 charges stop.
5. Rotate the Anthropic and Pinecone keys. They have lived in an ECS task
   definition as plain environment variables and in GCP Secret Manager.
6. After about a month, delete the `debate-chatbot` ECR repository and the
   remaining ECS log group.
