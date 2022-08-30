import json
import boto3  # Versão de Teste

region = 'us-east-2'
ec2 = boto3.client('ec2', region_name=region)


def lambda_handler(event, context): ## declarando uma funcao com argumento "event"
    instances = event["instances"].split(',')  #criando uma ver serparar com ","
    action = event["action"]  # declarar essa ação

    if action == 'Start':  # laço onde se for start faça isso
        print("STARTing you instances: " + str(instances))  #na conf do evento aponta id Successfully started instances: ['i-0e2902bf5cbb8ebf3', 'id_instance', 'id_instance']\""
        ec2.start_instances(InstanceIds=instances)
        response = "Successfully started instances: " + str(instances)
    elif action == 'Stop':  # se for stop faça isso
        print("STOPping you instances: " + str(instances)) #Successfully stopped instances: ['id_instance', 'id_instance', 'id_instance]\""
        ec2.stop_instances(InstanceIds=instances)
        response = "Successfully stopped instances: " + str(instances)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }




