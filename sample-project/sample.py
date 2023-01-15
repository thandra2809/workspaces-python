#!/usr/bin/env python3

# -*-coding:utf-8 -*-

"""A sample python code example for aws s3"""
import os

import boto3
from botocore.exceptions import ClientError

ACCESS_KEY = 'AWS_ACCESS_KEY_ID'
SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
BUCKET_NAME = 'thandra2809-sample-python'


def main():
    """entry point"""
    print('This is my First python project')
    access = os.getenv(ACCESS_KEY)
    secret_access_key = os.getenv(SECRET_ACCESS_KEY)
    s3 = boto3.resource('s3', aws_access_key_id=access, aws_secret_access_key=secret_access_key)

    create_bucket(BUCKET_NAME,s3)


def create_bucket(name, s3):
    try:
        bucket = s3.create_bucket(Bucket=name)
    except ClientError as ce:
        print('error', ce)


if __name__ == '__main__':
    main()
