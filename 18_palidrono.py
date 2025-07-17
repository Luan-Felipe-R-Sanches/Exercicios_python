'''
Crie um programa que pede que o usuário digite um nome ou uma frase, 
verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em tela esse resultado.
'''

frase = input('Digite uma palavra ou frase: ')

# Remove espaços e converte para minúsculas
frase_sem_espacos = ''.join(frase.split()).lower()

# Remove acentos e pontuação se quiser algo mais completo (opcional)

# Inverte a frase
frase_invertida = frase_sem_espacos[::-1]

# Exibe resultado
if frase_sem_espacos == frase_invertida:
    print('É um palíndromo!!!')
else:
    print('Não é um palíndromo.')
