'''
Crie um programa que pede ao usuário que o mesmo digite um número qualquer, 
em seguida retorne se esse número é primo ou não, 
caso não, retorne também quantas vezes esse número é divisível:
'''
numero = int(input('Digite um número: '))

if numero < 2:
    print(f'{numero} não é primo (números menores que 2 não são primos).')
else:
    divisoes = 0
    divisores = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisoes += 1
            divisores.append(i)

    if divisoes == 2:
        print(f'{numero} é primo!!!')
        print(f'{numero} é divisível apenas por 1 e por ele mesmo.')
    else:
        print(f'{numero} não é primo!!!')
        print(f'{numero} é divisível {divisoes} vezes.')
        print(f'Divisores: {divisores}')
