# definindo a fnção


# def func(a1, b2, c3, nome=None, h=5 ):  #def -> DEFININDO FUNÇÃO func -> PROPRIA FUNÇÃO () -> ar
#     print(a1, b2, c3, nome, h)  # ARGUMANTOS DA FUNÇÃO
#     return h, nome, b2
#
# var = func(1, 2, 3, nome='Fernando', h='horas')  # DECLARANDO AS PROPRIEDADES DO ARGUMENTO
# print(var)



def func(*args):
    print(args[-1])
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
print(*lista, sep='|')
