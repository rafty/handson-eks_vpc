#!/usr/bin/env python3
import os
import aws_cdk as cdk
from stacks.vpc_stack import VpcStack


app = cdk.App()

env = cdk.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]),
)

# vpc_name = 'gitops_pipeline'
vpc_name = app.node.try_get_context('vpc_name')
VpcStack(
    app,
    "EksVpcStack",
    vpc_name=vpc_name,
    vpc_cidr='10.11.0.0/16',
    env=env)

app.synth()
