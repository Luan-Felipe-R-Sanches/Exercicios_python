def soma(*args):
    num = 0
    for valordigitado in args:
        num += valordigitado
    print(f'O resultado da soma é: {num}')

soma(18, 43, 99, 1)
