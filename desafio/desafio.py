"""

nome = 'Fernando Horas'
altura = 1.79
ano_nasc = 1981
ano_atual = 2022
peso = 79
idade = 41
imc = peso / (altura ** 2)
idade_atual = ano_atual - idade


print(f'{nome} tem {idade} anos, seu ano de nascimento é {idade_atual} e sua altura é {altura} '
      f'de altura e seu peso é de: {peso} kilos e seu IMC é de: {imc:.2f}')
"""

# Input
"""
nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
ano_nascimento = 2022 - int(idade)  #fazendo cache

print()
print(f'{nome} sua idade é: {idade} anos. '
      f'{nome} você nasceu em {ano_nascimento}.')

"""

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite segundo numero: ')
resultado = int(numero_1) + int(numero_2)

print()
print(f'A soma dos numeros informados é {resultado}. ')




