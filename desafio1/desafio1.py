""""
Faça um progra que peça ao usuario pra digitar um numero inteiro, inform que esse numero é par ou impar. caso
o usuario não digite um número inteiro, informe que não é um numero inteiro.
"""


""" 
numero_inteiro = input('Digite um número inteiro: ')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é Par')
    else:
        print(f'{numero_inteiro} é Impar')

else:
    print('Isso não é um número inteiro. ')

"""





"""
Faça um programa que pergunte a hota para o usuario e, baseando-se no horario descrito, exibe a saudação apropriada 
ex: BOm dia 0-11 boat tarde 12-17 boa noite 18-23
"""

""" 
horario = input('Digite um horario entre 0 e 23 : ')


if horario.isdigit():  # SIGINIFIGA - SE é um numero entra caso for outra coisa pula else
    horario = int(horario)

    if horario < 0 or horario > 23:
        print()
        print('Horario deve está entre 0 e 23. ')
    else:
        if horario <= 11:
            print()
            print(f'{horario}:00 hrs, bom dia! ')
        elif horario <= 17:
            print()
            print(f'{horario}:00 hrs,Boa tarde! ')
        else:
            print()
            print(f'{horario}:00 hrs,Boa noite!')
else:
    print()
    print('ATENÇÃO!! Por favor digita uma horario entre 0 e 23.')


"""

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva "seu nome é curto; 
se tiver entre 5 e 6 letras. escreva "Seu nome é ormal"; maior que 6 escreva "Seu nome é muito grande"

"""

""" 

nome = input("DIgite seu NOme: ")
tamanho = len(nome)


if tamanho <= 4:
    print(f'{nome}, esse nome é Curto ')
elif tamanho <= 6:
    print(f'{nome}, esse nome é Normal. ')
else:
    print(f'{nome}, esse nome é muito grande.')

"""







""" 

texto = 'Fernando Horas'

print(texto[0])
"""





# ENTENDER CONSIGÕES E OPERADORES (laços de repsdições)fer

""" 
while True:  # enquanto for verdadeiro executa isso - loop infinido
    nome = input('Qual é seu nome: ')
    print(f'Olá {nome} !')


print("Não será executado.")

"""



""" 
cont = 0
while cont < 5:
    if cont == 3:
        cont = cont + 1
        break ## apos encontar o 3 ele finaliza 
    print(cont)
    cont = cont + 1
print('Finalizado! ')

"""


""" 
cont = 0
while cont < 5:
    if cont == 3:
        cont = cont + 1
        continue ## apos encontrar ele pula o 3 e continua 
    print(cont)
    cont = cont + 1
print('Finalizado! ')

"""

""" 


x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'({x}, {y})')
        y += 1
    x += 1
print(" Acabou! ")
"""
#
# print()
# print(
#     print(
#         print(
#
#         )
#     )
# )


frase = ' O rato rieu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual é a letra que deseja coloca maiúscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)

















