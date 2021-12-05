import urllib
import boto3
import ast
import json
print('Loading function')

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    sns_message = ast.literal_eval(event['Records'][0]['Sns']['Message'])
    target_bucket = context.function_name[:-1]
    source_bucket = str(sns_message['Records'][0]['s3']['bucket']['name'])
    key = str(urllib.unquote_plus(sns_message['Records'][0]['s3']['object']['key']).decode('utf8'))
    print "Deleteing %s from bucket %s ..." % (key, target_bucket)
    obj = s3.Object(target_bucket, key)
    try: 
        obj.load()
        obj.delete()
    except:
        print("Did not delete.")
    
