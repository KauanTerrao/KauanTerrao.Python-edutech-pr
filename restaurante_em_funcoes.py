def imprime_cardapio():
    print('Especificacao   Codigo  Preco')
    print('Cachorro Quente 100     R$ 1,20')
    print('Bauru Simples   101     R$ 1,30')
    print('Bauru com Ovo   102     R$ 1,50')
    print('Hamburger       103     R$ 1,20')
    print('Cheeseburger    104     R$ 1,30')
    print('Refrigerante    105     R$ 1,00')


def soma_produtos():

    codigo = 100
    while codigo >= 100 and codigo <= 105:
        codigo = int(input('Informe o codigo do produto ou um codigo invalido para encerrar: '))

        if codigo >= 100 and codigo <= 105:

            quantidade = int(input('Informe a quantidade: '))
            if codigo == 100:
                valor_item = 1.20 * quantidade
            elif codigo == 101:
                valor_item = 1.30 * quantidade
            elif codigo == 102:
                valor_item = 1.50 * quantidade
            elif codigo == 103:
                valor_item = 1.20 * quantidade
            elif codigo == 104:
                valor_item = 1.30 * quantidade
            elif codigo == 105:
                valor_item = 1.0 * quantidade

        print('Valor do item: %.2f' % valor_item)

imprime_cardapio()
soma_produtos()