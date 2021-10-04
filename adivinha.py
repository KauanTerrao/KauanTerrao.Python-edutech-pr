import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    print("(1) Facil / (2) Medio / (3) Dificil")

    nivel = int(input("Escolha a dificuldade desejada:"))

    numero_secreto = random.randrange(1, 101)
    round(numero_secreto)
    total_de_tentativa = 0
    tentativa_atual = 1
    pontuacao = 0

    if nivel == 1:
        total_de_tentativa = 20
        print("Você acaba de selecionar o modo facil, você terá {} tentativas!".format(total_de_tentativa))
    elif nivel == 2:
        total_de_tentativa = 10
        print("Você acaba de selecionar o modo mediano, você terá {} tentativas!".format(total_de_tentativa))
    else:
        total_de_tentativa = 5
        print("Você acaba de selecionar o modo mais dificil, você terá apenas {} tentativas".format(total_de_tentativa))

    pontuacao = 1000

    for tentativa_atual in range(1, total_de_tentativa + 1):
        print("Tentativas {} de {}".format(tentativa_atual, total_de_tentativa))
        chute_str = input("Digite o seu número:")
        print("Você digitou", chute_str)
        chute = int(chute_str)
        soma = 0

        if chute <= 0 or chute > 100:
            print("Ô seu animal, não saber ler não? É entre 1 há 100.")
            continue

        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if acertou:
            soma = abs(chute - numero_secreto)
            pontuacao = pontuacao - soma
            print("Fim de jogo! Você acertou! Sua pontuação foi: {}".format(pontuacao))
            break
        else:
            if maior:
                soma = abs(chute - numero_secreto)
                pontuacao = pontuacao - soma
                print("Você errou, o número chutado foi maior que a resposta!")
                print("Agora sua pontuação é {}.".format(pontuacao))
            elif menor:
                soma = abs(chute - numero_secreto)
                pontuacao = pontuacao - soma
                print("Você errou, o número chutado foi menor que a resposta!")
                print("Agora sua pontuação é {}.".format(pontuacao))

        # if chute != numero_secreto:
        # soma = abs(chute - numero_secreto)
        # pontuacao = pontuacao - soma
        # print("Você errou, agora a sua pontuação é". format(pontuacao))

        if pontuacao <= 0:
            print("Fim de jogo, você ficou sem pontos!")
            break

    print("O número certo era", numero_secreto)


if __name__ == "__main__":
    jogar()
