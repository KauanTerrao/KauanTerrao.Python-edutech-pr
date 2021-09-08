def calcula():
    print("(1) soma, (2) subtração, (3) divisão, (4) multiplicação, (5) potencialização")
    operacao = int(input("Qual operação deseja realizar?"))
    numerox = int(input("Qual o primeiro número a ser utilizado?"))
    numeroy = int(input("Qual o segundo número a ser utilizado?"))

    if operacao == 1:
        soma(numerox, numeroy)
    elif operacao == 2:
        subtracao(numerox, numeroy)
    elif operacao == 3:
        divisao(numerox, numeroy)
    elif operacao == 4:
        multiplicacao(numerox, numeroy)
    elif operacao == 5:
        potencializacao(numerox, numeroy)


def divisao(numerox, numeroy):
    print(numerox / numeroy)


def multiplicacao(numerox, numeroy):
    print(numerox * numeroy)


def potencializacao(numerox, numeroy):
    print(numerox ** numeroy)


def soma(numerox, numeroy):
    print(numerox + numeroy)


def subtracao(numerox, numeroy):
    print(numerox - numeroy)


calcula()
