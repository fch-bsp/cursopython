import json
import boto3  # Versão de Teste

region = 'us-east-2'
ec2 = boto3.client('ec2', region_name=region)


def lambda_handler(event, context):
    instances = event["instances"].split(',')
    action = event["action"]

    if action == 'Start':
        print("STARTing you instances: " + str(instances))
        ec2.start_instances(InstanceIds=instances)
        response = "Successfully started instances: " + str(instances)
    elif action == 'Stop':
        print("STOPping you instances: " + str(instances))
        ec2.stop_instances(InstanceIds=instances)
        response = "Successfully stopped instances: " + str(instances)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
