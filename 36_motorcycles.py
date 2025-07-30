# Criando uma lista de motocicletas
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Substituindo o primeiro elemento
motorcycles[0] = 'ducati'
print(motorcycles)

# Adicionando um novo elemento ao final da lista
motorcycles.append('ducati')
print(motorcycles)

# Criando uma nova lista vazia e adicionando elementos
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Inserindo um elemento em uma posição específica
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removendo um elemento usando a instrução del
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Removendo o último elemento com o método pop
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

# Removendo outro elemento com pop e usando o valor
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Removendo um elemento pelo valor
motorcycles.remove('ducati')
print(motorcycles)


