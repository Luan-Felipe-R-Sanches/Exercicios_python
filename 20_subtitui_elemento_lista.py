# Dada a seguinte lista: nomes = [‘Ana’, ‘Carlos’, ‘Daiane’, ‘Fernando’, ‘Maria’], substitua o terceiro elemento da lista por ‘Jamile’:
nomes = ['Ana', 'Carlos', 'Daine', 'Fernando', 'Maria']

nomes[2] = 'Jamile'
print(nomes)

# Adicione o elemento ‘Paulo’ na lista nomes
nomes = ['Ana', 'Carlos', 'Jamile', 'Fernando', 'Maria']
nomes.append('Paulo')
print(nomes)

# Adicione o elemento ‘Eliana’ na lista nomes, especificamente na terceira posição da lista
nomes = ['Ana', 'Carlos', 'Jamile', 'Fernando', 'Maria', 'Paulo']
nomes.insert(2, 'Eliana')
print(nomes)

# Remova o elemento ‘Carlos’ da lista nomes:
nomes = ['Ana', 'Carlos', 'Jamile', 'Fernando', 'Maria', 'Paulo']
nomes.remove('Carlos')
print(nomes)

# Mostre o segundo, terceiro e quarto elemento da lista nomes. Separadamente, mostre apenas o último elemento da lista nomes
nomes = ['Ana', 'Carlos', 'Jamile', 'Fernando', 'Maria', 'Paulo']
print(nomes[1:4])
print(nomes[-1])