import os
import random

def limpar_tela():
    """Limpa o console"""
    input("\nPressione 'ENTER' para continuar...")    
    os.system("cls")
    imprimir_cabecalho()

def imprimir_cabecalho():
    cab = """
    ************************************************************
    *                      Jogo da Velha                       *
    ************************************************************
    """
    print(cab)

def ler_nomes():
    """ Lê os nomes dos jogadores e retorna em uma lista"""
    print("Olá, bem vindo ao jogo da velha!")
    print("Primeiramente, quero saber os nomes de quem está jogando...")
    jog1 = input("Jogador 1, digite seu nome:")
    jog2 = input("Jogador 2, digite seu nome:")
    jogador = [jog1,jog2]
    return jogador

def sortear_jogador(jogador):
    print(f"{jogador[0]}, você jogara com 'O'")
    print(f"{jogador[1]}, você jogara com 'X'")
    print("...Sorteando quem inicia o jogo...")
    vez = random.choice([0,1])
    print(f"{jogador[vez]}, você começa!")
    return  vez

def criar_matriz_jogo():
    mat = []
    for i in range(3):
        mat.append([" "]*3)
    return mat

def print_matriz(mat):
    for i in range(3):
        print("._.._.._.")
        for j in range(3):
            print(f"|{mat[i][j]}|",end="")
        print("")

def verif_resultado(mat,jogador,simb,vez,rodada):
    result = False
    if rodada < 4:
        return result
    elif rodada <= 8: #testa se alguem venceu
        s = simb[vez]
        #testar linhas
        for i in range(3):
            if mat[i] == [s,s,s]:
                result = True
                break

        #testar colunas
        for i in range(3):
            if mat[i][0] == s and mat[i][1] == s and mat[i][2] == s:
                result = True
                break

        #testar diagonais
        if mat[0][0] == s and mat[1][1] == s and mat[2][2] == s:
                result = True
        if mat[0][2] == s and mat[1][1] == s and mat[2][0] == s:
                result = True

        if result:
            print(f"Parabéns, {jogador[vez]}, você foi o vencedor!")
        else:
            if rodada == 8:
                print(f"Houve empate entre os jogadores!")
                result = True
        return result


def jogar(jogador,simb,vez):
    limpar_tela()
    mat = criar_matriz_jogo()
    rodada = 0
    result = False
    while(not result):
        #ler jogada
        vez = vez%2
        print(f"{jogador[vez]}, é sua vez:")
        print_matriz(mat)
        l,c = map(int,input("Digite o valor da linha e coluna que deseja jogar separado por espaço:").split(" "))
        mat[l][c] = simb[vez]
        limpar_tela()
        result = verif_resultado(mat,jogador,simb,vez,rodada)
        vez +=1
        rodada +=1   

    
    
    
    
    
    
    
    
    
    