var = 0
while var <= 10:
    print(var)
    var = var + 1
    
# percorre a string e mostra letra por letra
for i in'Nikola Tesla':
    print(i)
    
# lista com for

lista10 = ['Água', 'Açúcar', 'Arroz', 'Pão', 'Leite', 'Carne', 'Refrigerante']
for i in lista10:
    print(i)

"""
Crie um programa que lê um valor de início e um valor de fim, 
exibindo em tela a contagem dos números dentro desse intervalo.
incio = int(input('Digite o número onde começa a contagem: '))
fim = int(input('Digite o número onde termina a contagem: '))

for i in range(incio, fim+1):
    print(i)
"""
    
"""
Crie um programa que realiza a contagem de 0 a 20, exibindo apenas os números pares:
"""
for i in range(0, 21):
    if i % 2 == 0:
        print(i)
        
for i in range(0,21,2):
    print(i)