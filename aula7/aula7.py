nome = 'Fernando Horas'
idade = 41
altura = 1.79
e_maior = idade > 18
peso = 89
imc = peso / (altura ** 2)


print(nome, 'tem', idade, 'anos de idade e seu IMC é de:', imc)
print(f'{nome} tem {idade} anos de idade e seu imc  de de: {imc:.2f}')
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im}'.format(n=nome, i=idade, im=imc))

