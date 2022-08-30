"""
import json
import boto3

region = 'us-east-2'
ec2 = boto3.client('ec2, region_name=region')



def lambda_handler(event, context):  #função criada
    instances = event["Instances"].split(',')
    action = event["action"]

    if action == 'start':
        print("instancia foi ligada" + str(instances))
        ec2.start_instances(instancesids=instances)
        response = "Instancia ligada com sucesso: " + str(instances)
    elif action == "stop":
        print("instancia foi ligada" + str(instances))
        ec2.stop_instances(instancesids=instances)
        response = "Instancia deslifada com sucesso: " + str(instances)

        return {
            'statusCode': 200,
            'body': json.dump(response)

        }
"""
""" 
def lambda_handler(event, context):
    instances = event["instances"].split(',')
    action = context["action"]
    print(instances, action)

lambda_handler(isinstance= 'tste', action='kdnkdnk')
"""





""" 

def conta_maio (carro, seguro, estacionamento):
    return carro + seguro + estacionamento
banco = conta_maio(1100, 142, 2210)

print(f'O total de pagamento esse mês é: R$ {banco},00.')
"""

""" 

def divisao (n1, n2):
    if n2 == 0:
        return

    return n1 / n2
divide = divisao(8, 0)

if divide:
    print(divide)
else:
    print('conta inválida.')

"""



""" 


def conta_maio (carro, seguro, estacionamento):  # informa função e os atributos
    return carro + seguro + estacionamento  # retorna os valores dos atributos
pagamento = conta_maio(1200, 258, 254)  # variavél com a função de propriedade
print()  # pular linha


print(f'O valor total referente aos gasto foi de: R$ {pagamento},00.')
"""





def contas_maio(carro, seguro, estacionamento):
    return carro + seguro + estacionamento
valor = contas_maio(1200, 255, 125)

print(f'O valor que vou pagar esse mê é: R$ {valor},00')








































































































