def boas_vindas(nome, nacionalidade="Brasileiro"):
    print(f'{nome} é {nacionalidade}!!!')

# Entrada de dados e chamadas da função fora da definição
nome = input('Digite o seu nome: ')
boas_vindas(nome)  # Usa a nacionalidade padrão

nacionalidade = input('Digite sua nacionalidade: ')
boas_vindas(nome, nacionalidade)  # Usa a nacionalidade informada
