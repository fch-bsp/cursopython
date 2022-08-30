## Sistema pra chegar usuario e senha



usuario = input('Nome do usuario: ')  #infomação do user str
senha = input('Senha do Usuário: ')  #informação di user str

user_bd = 'fernando'  # informação do nosso banco de dados
senha_bd = '123456'  # informação do nosso banco de dados


if user_bd == usuario and senha_bd == senha:
    print(f'{usuario}, Seja bem vido ao nosso sistema.')
else:
    print('Usuário e senha inválido')


