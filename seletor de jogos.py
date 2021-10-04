import forca
import adivinha

print("-------------------------------------------------------------------------------------------------------------")
print("                                             Escolha algum jogo")
print("-------------------------------------------------------------------------------------------------------------")

print(" (1) Jogo da Forca / (2) Jogo de adivinhação")

jogo = int(input("Qual será o jogo?"))

if jogo == 1:
    print("iniciando o a Forca...")
    forca.jogar()
elif jogo == 2:
    print("Iniciando a adivinhação...")
    adivinha.jogar()
