'''
Crie um dicionário via método construtor dict( ), atribuindo para o mesmo ao menos 5 
conjuntos de chaves e valores representando objetos e seus respectivos preços:
'''
dicionario = dict(
    Pão = 'R$ 1,99',
    Açúcar = 'R$ 4,99',
    Café = 'R$ 3,49',
    Macarrão = 'R$ 3,99',
    Carne = 'R$ 16,99',
                  )
print(dicionario)

# Crie um dicionário usando o construtor de dicionários do Python, alimente os valores do mesmo com os dados de duas listas
itens = ['Caneta', 'Lápis', 'Borracha', 'Caderno']
precos = ['1,99', '0,99', '0,50' , '9,90']

dicionario1 = dict(keys = itens, values = precos)
print(dicionario1)
print(type(dicionario1))

# Crie uma simples estrutura de dados simulando um cadastro para uma loja. Nesse cadastro deve conter informações como nome, 
# idade, sexo, estado civil, nacionalidade, faixa de renda, etc... Exiba em tela tais dados

cadastro = {'Nome':'Paulo',
            'Sexo':'Masculino',
            'Idade':38,
            'Nacionalidade':'Brasileiro',
            'Estado Civil':'Divorciado',
            'Escolaridade':['Ensino Superior',
                            'Doutorado'],
            'Ocupação':'Professor',
            'Renda':'1999.00-29999.00'}
print(cadastro)

# Crie um programa que recebe dados de um aluno como nome e suas notas em supostos 3 trimestres de aula,
# retornando um novo dicionário com o nome do aluno e a média de suas notas

aluno = [{'Nome':'Fernando','Notas':[62,73,90]}]

def calcula_media(aluno):
    notas = []
    for media in aluno:
        if len(media['Notas'])>0:
            temp = round(sum(media['Notas'])/len(media['Notas']))
        else:
            temp = 0
            notas.append({'Nome':media['Nome'],'Média das notas':temp})
            print(notas)
            
            media_estudante = calcula_media(aluno)