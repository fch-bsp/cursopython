"""
CRIE UMA FUNÇÃO QUE EXIBE UMA SAUDAÇÃO COM OS PARAMÊTROS: SAUDACAO E NOME E
MOSTRE NA TELA.
"""



# def saudacao(saudacao, nome):
#     print(f'{saudacao}, {nome}')
#
#
# saudacao('Olá', 'Fernando')
# saudacao('Hi', 'Horas')
# saudacao('Hello', 'nando')
# saudacao('Fala', 'NIm')


"""
CRIE UMA FUNÇÃO QUE REVEBE 3 NUMEROS COMO PARAMETRO E EXIBA A SOMA ENTRE ELES.

"""


# def soma(n1, n2, n3):
#     print(f'A soma dos trê números é', (n1 +n2 + n3))
#
# soma(1, 3, 3)
# soma(1, 1, 1)
# soma(3, 1, 1)

"""
funcao de aumento porcentual
"""



# def aumento_porcentual(valor, porcentual):
#     return valor + (valor * porcentual / 100)
#
# ap = aumento_porcentual(50, 10)
# print(ap)
# ap = aumento_porcentual(100, 10)
# print(ap)
# ap = aumento_porcentual(10, 10)
# print(ap)
# ap = aumento_porcentual(15, 100)
# print(ap)



#
# def seu_nome(nome, sobrenome):
#     print(f'Seu nome é:{nome} e seu sobrenome é:{sobrenome}.')
#
# seu_nome('Fernando', 'Horas')
#



def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return f'fizzbuzz, {n} é divissível por 3 e 5'
    if n % 5 == 0:
        return f'buzz, {n} é divissível por  5'
    if n % 3 == 0:
        return f'fizz, {n} é divissível por 3'
    return n


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fb(aleatorio))





























































