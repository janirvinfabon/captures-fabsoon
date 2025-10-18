#!/bin/bash
cd backend/
echo "Running: sls deploy --config serverless.yml --region ap-southeast-1 --aws-profile $AWS_PROFILE --verbose$@"
sls deploy --config serverless.yml --region ap-southeast-1 --aws-profile $AWS_PROFILE --verbose "$@"