class TiposDeVariaveis:
    variavelGlobal = 10

    def mostrar_valores(self):
        variavelLocal = 5
        print(f"Valor da variável global: {self.variavelGlobal}")
        print(f"Valor da variável local: {variavelLocal}")


if __name__ == "__main__":
    variaveis = TiposDeVariaveis()
    variaveis.mostrar_valores()
