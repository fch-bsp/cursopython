# Criar uma calculadora basico

# criar um loop infinido

"""

print('Opção: 1 Informa o primeiro numero:')
print('Opção: 2 Informa o segundo numero:')
print('Opção: 3 Informa qual soma deseja fazer  Ex: soma + adição - diviçao / multiplicação * . ')
print()


while True:  # enquanto  for verdadeiro EXECUTE ESSE LAÇO
    print()  # pula linha
    num_1 = input('Digite um número: ')  # criei uma variavel e usei input pra receber valor dig
    num_2 = input('Digite outro número: ')# criei uma variavel e usei input pra receber valor dig
    operador = input('Qual operação deseja executar: ')# criei um operador que vai fazer oper

    if not num_1.isnumeric() or not num_2.isnumeric():  # SE NÃO for var x um numero E  var y num
        print('Você precisa digitar um numero ')  # Informa que
        continue  # continue apos informa valor obrigatório
    num_1 = int(num_1)  # tranformei var str numa var int
    num_2 = int(num_2)  # tranformei var str numa var int

    if operador == '+':  # SE op digitado for igual a '+"
        print(num_1 + num_2) # soma as var informada

    elif operador == '-':  # SE op digitado for igual a '-"
        print(num_1 - num_2)  # sadicão as var informada
    elif operador == '/':  # SE op digitado for igual a '/"
        print(num_1 / num_2)  # div as var informada
    elif operador == '*':  # SE op digitado for igual a '*"
        print(num_1 * num_2)  # mult as var informada
    else:  #Se não for cai aqui
        print('Operador invalido!')  # informa essse valor
"""


""" 
# Conceito de Contador

contador = 50
while contador < 100:
    print(contador)
    contador += 1
    
"""


"""

# Conceito de acumuladores

contador = 1
acumuladores = 1
while contador <= 10:
    print(contador, acumuladores)
    if contador < 5:
        break
    acumuladores = acumuladores + contador
    contador += 1

else:
    print(' Cheguei no Else. ')

"""




frase = 'Eu sou o rei de roma porra '
tamamanho_frase = len(frase)
print(tamamanho_frase)
