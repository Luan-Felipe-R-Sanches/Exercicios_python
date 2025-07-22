""" Crie uma função que recebe um valor digitado 
pelo usuário e eleva esse valor ao quadrado """

def exp(num):
    return num ** 2
num = int(input('Digite um número: '))
num = exp(num)
print(num)