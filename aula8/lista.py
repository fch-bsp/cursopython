"""

Função Split, join, enumerate

"""


#
# string = "O Brasil é o pais do futebol, o Brasil é penta."
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# palavra = ' '
# contagem = 0
#
# for valor in lista_2:
#     print(valor.strip().capitalize())  #.strip retira espaço e o .capitalize troca caixa baixa por caixa alta



# for valor in lista_1:
#     qtde_vezes = lista_1.count(valor)
#
#     if qtde_vezes > contagem:
#         contagem = qtde_vezes
#         palavra = valor
#
# print(f'A palavra que aparceu mais vezes é {palavra} ({contagem} x) ')
#

# JOIN

#
# string= 'O Brasil é penta'
# lista = string.split(' ')
# string2 = '|'.join(lista)
#
# print(string)
# print(lista)
# print(string2)



# ENUMERATE


# string= 'O Brasil é penta'
# lista = string.split(' ')
#
#
# for indice, valor in enumerate (lista):
#     print(indice, valor)



# lista = ['fernando', 'priscila', 'klara']
#
# for indice, nome in enumerate(lista):
#     print(indice, nome)
#

#
# lista = [
#   # indce lista
#     #   0           1           2
#     ['fernando', 'priscila', 'klara'],  # 0
#       #0       #1        #2
#     ['caia', 'neuza', 'julia'],  # 1
#
#         #0        #1        #2
#     ['vanessa', 'marcus', 'duda'],  # 2
#
#
# ]
#
#
#
# print(lista[1][1])



# Trocar valores de variavéis




# x = 10
# y = 'fernando'
#
# x, y = y, x
#
# print(f'x={x}, y={y}')



"""
Operador ternário em Python
"""

# logar_user = True
#
# if logar_user:
#     msg = 'Usuario Logado'
# else:
#     msg = 'Usuario precisar logar'
#
# print(msg)


# logar_user = False
#
# msg = 'Úsuario Logado. ' if logar_user else 'Usuario precisa logar.'
#
#
# print(msg)
#


idade = 18

if idade >= 18:
    print('Pode acessar sistema.')
else:
    print('Não pode acessar sistema. ')




















































