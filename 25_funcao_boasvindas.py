def boas_vindas(nome, sobrenome):
    print(f'Bem vindo(a) {nome} {sobrenome}')

nome = input('Digite o seu nome: ')
sobrenome = input('Agora digite o seu sobrenome: ')

pessoa = boas_vindas(nome, sobrenome)