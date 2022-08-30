"""
Criar um sistema de validador de CPF:

ESCOPO DO PROJETO:::

EXEMPLO:

CPF: 258.128.658-09
----------------------------------------------------------------
2 * 10 = 10    *        1 * 11 = 11
5 * 9  = 54    *        6 * 10 = 60
8 * 8  = 64    *        8 * 9  = 72
1 * 7  = 63    *        9 + 8 =  72
2 * 6  = 54    *        9 + 7  = 63
8 * 5  = 25    *        5 * 6  = 30
6 * 4  = 12    *        3 * 5  = 15
5 * 3  = 15    *        5 * 4 =  20
8 * 2  = 0     *        0 * 3  = 0
                        0 8 2  = 0

                                  343
                         11 - (343 % 11 ) = 9

                         Digitos  2 = 9



          297
11 - (297 % 11) = 11
11 > 9 = 0
Digito 1 = 0

============================================================================================================

"""
#VALIDADOR DE CPF

# while True:
#     cpf = input('Digite um CPF: ')
#     novo_cpf = cpf[:-2]
#     reverso = 10
#     total = 0
#
#     for index in range(19):
#         if index > 8:
#             index -= 9
#
#         total += int(novo_cpf[index]) * reverso
#
#         reverso -= 1
#         if reverso < 2:
#             reverso = 11
#             d = 11 - (total % 11)
#
#             if d > 9:
#                 d = 0
#             total = 0
#             novo_cpf += str(d)
#
#
#     if cpf == novo_cpf:
#         print("CPF Válido.")
#     else:
#         print("CPF Inválido.")





## GERADOR  DE CPF VÁLIDOS

from random import randint
numero = str(randint(100000000, 999999999))



novo_cpf = numero
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)


print('O CPF Válido gerado é:')
print(novo_cpf)
























