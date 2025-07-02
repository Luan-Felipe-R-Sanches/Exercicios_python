def boas_vindas():
    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite o seu sobrenome: ")

    mensagem = f"Bem-vindo,{nome} {sobrenome}"
    print(mensagem)


if __name__ == "__main__":
    boas_vindas()
