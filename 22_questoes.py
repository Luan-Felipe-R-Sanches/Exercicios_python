"""
Crie um sistema de perguntas e respostas que interage com o usuário, pedindo que o mesmo insira uma resposta.
Caso a primeira questão esteja correta, exiba em tela uma mensagem de acerto
e parta para a próxima pergunta, caso incorreta, exiba uma mensagem de erro e pule para próxima pergunta
"""

# Dicionário contendo as perguntas, alternativas e a resposta correta de cada pergunta
base = {
    "Pergunta 01": {
        "pergunta": "Quanto é 4X4 ?",
        "alternativas": {"a": "12", "b": "24", "c": "16", "d": "20"},
        "resposta_certa": "c",  # alternativa correta é 'c' (16)
    },
    "Pergunta 02": {
        "pergunta": "Quanto é 6 / 3 ?",
        "alternativas": {"a": "2", "b": "1", "c": "3", "d": "4"},
        "resposta_certa": "a",  # alternativa correta é 'a' (2)
    },
}

respostas_certas = 0  # contador para o número de respostas corretas

# Loop para percorrer todas as perguntas no dicionário 'base'
for pkeys, pvalues in base.items():
    # Exibe o identificador da pergunta e o texto da pergunta
    print(f'{pkeys}: {pvalues["pergunta"]}')

    # Solicita ao usuário que escolha uma alternativa
    resposta = input("Escolha uma alternativa: [a], [b], [c] ou [d]: ")

    # Verifica se a resposta do usuário é igual à alternativa correta
    if resposta == pvalues["resposta_certa"]:
        print("Resposta Correta!!!")
        respostas_certas += 1  # incrementa o contador de respostas certas
    else:
        print("Resposta Incorreta!!!")

# Após responder todas as perguntas, informa ao usuário o total de acertos
if respostas_certas == 0:
    print("Você não acertou nenhuma questão.")
elif respostas_certas == 1:
    print("Você acertou apenas uma questão.")
else:
    print("Você acertou todas as questões.")
