from funcoesJogo import *

#iniciarJogo
imprimir_cabecalho()

#ler nomes
jogador = ler_nomes()

#sortear iniciante
simb = ["O","X"]
vez = sortear_jogador(jogador)

jogando = True
while(jogando):
    jogar(jogador,simb,vez)
    if input("Deseja jogar outra? 'S' ou 'N':").upper() == "N":
        jogando = False