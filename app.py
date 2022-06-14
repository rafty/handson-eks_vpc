#!/usr/bin/env python3
import os
import aws_cdk as cdk
# from create_vpc.create_vpc_stack import CreateVpcStack
from stacks.vpc_stack import VpcStack


app = cdk.App()

env = cdk.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]),
)

vpc_name = 'gitops_pipeline'
VpcStack(
    app,
    "CreateVpcStack",
    vpc_name=vpc_name,
    vpc_cidr='10.11.0.0/16',
    env=env)

app.synth()
