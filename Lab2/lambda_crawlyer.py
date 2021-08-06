import json
import datetime
import random
import boto3
import csv
import io

kinesis = boto3.client('kinesis', region_name='cn-northwest-1') #<--- 调整 region 如果您不在 cn-northwest-1,例如调整为 us-east-2

def lambda_handler(event, context):

    bigdataStreamName = "test_stream"#<--- 调整 StreamName 为您在之前实验中的Kinesis dataStream名字
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket="partner-workshops-cn-northwest-1", Key="data/partial-load/ratings-partial-load.csv")#<--- response返回是读取模拟数据的路径，不需要调整
    tsv =  str(response['Body'].read().decode('UTF-8'))
    lines = tsv.split("\n")
    for line in tsv.split("\n"):
        val = line.split(",")
        data = json.dumps(getRating(val[0], val[1], val[2], val[3]))
        kinesis.put_record(StreamName=bigdataStreamName, Data=data, PartitionKey="rating")
    return "complete"

def getRating(userId, itemId, ratingId, timestamp):
    data = {}
    data['userid'] = userId
    data['movieid'] = itemId
    data['ratingid'] = ratingId
    data['timestamp'] = timestamp
    return data


