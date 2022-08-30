"""
CONDIÇÕES DE IF, ELIF e ELSE

"""
""" 
if False:  # SE NÃO FOR VERDADEIRO FAÇA ISSO
    print('Verdadeiro.')
elif False:  # AINDA NÃO PODE EXECUTAR
    print('Ainda não é verdadeiro')
    print('mais alguma coisa')
elif True:  # AGORA SIM!! É VERDADEIRO E FAÇA ISSO
    print('Agora sim!! é verdadeira.')
    nome = input('qual seu nome? ')
    print(f'seu nome é {nome}.')
else:
    print('Não é verdadeiro.')
    print(2 + 20)

"""




"""
OPERADORES RELACIONAIS
"""



## CRIAR UM PROGRAMA QUE VERIFICA A IDADE PARA APROVAR OU NÃO EMPRESTIMO


## CRIANDO AS VARIAVEIS

"""

nome = input("Qual é seu nome? ")  ## srting
idade = input('Qual sua idade? ')  ## string
idade = int(idade)  ## converter idade para inteiro
idade_limite = 18

if idade >= idade_limite:
    print(f"{nome}, PARABÉNS!!!você está autorizado a pegar o empréstimo por ter {idade} anos.")
else:
    print(f"{nome}, QUE PENA!! NÃO pode pegar o emprestimo por ter {idade} anos e o limite minimo é {idade_limite}")

"""




nome = input("Qual é seu nome? ")  ## srting
idade = input('Qual sua idade? ')  ## string
idade = int(idade)  ## converter idade para inteiro
idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f"{nome}, PARABÉNS!!!você está autorizado a pegar o empréstimo por ter {idade} anos.")
else:
    print(f"{nome}, QUE PENA!! NÃO pode pegar o emprestimo por ter {idade} ")


























