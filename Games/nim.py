import random

def menu():
    # Função para mostrar o menu com as opções do jogo
    print("""
0 - Sair
1 - Humano vs Humano
2 - Humano vs Computador
    """)

    option = -1  # Entra no loop e aguarda uma opção que seja válida do jogador, ou seja, 0,1 ou 2
    while option not in (0, 1, 2):
        # Recebe a opção do jogador até que seja uma opção válida (0, 1 ou 2)
        option = int(input("Opção:"))

    if option == 1 or option == 2:
        # Inicia o jogo com a opção escolhida pelo jogador
        iniciarJogo(option)
    elif option == 0:
        # Encerra o jogo
        print("Obrigado por jogar o meu jogo!")

def gerarTabuleiro():
    # Função para gerar um tabuleiro com quatro pilhas com valores aleatórios entre 1 e 30
    tabuleiro = []
    for i in range(0, 4):
        tabuleiro.append(random.randint(1, 30))
    return tabuleiro

def mostrarTabuleiro(tabuleiro):
    # Função para exibir o estado atual do tabuleiro
    print("Tabuleiro:", *tabuleiro)

# len -> length
def validarJogada(jogadas, tabuleiro):
    # Função para verificar se as jogadas são válidas (comparando com o tabuleiro que tem 4 pilhas)
    if len(jogadas) != 4:
        return False
    # contar o numero de jogadas que o usuario digitou (numero de pilhas -> max 2, min 1)
    total_jogadas = 0
    for jogada in jogadas: # lê-se "para cada elemento dentro da lista jogadas, repetir...
        if jogada > 0:
            total_jogadas = total_jogadas + 1
    # Verificar se o total de jogadas é = 0 ou superior a 2 (não se pode tirar de mais de 2 pilhas)
    if total_jogadas == 0 or total_jogadas > 2:
        return False
    # TABULEIRO = [7, 29, 14, 2]
    # JOGADA = [7, 20, 0, 0]
    for i in range(0, len(jogadas)):
        if jogadas[i] < 0 or jogadas[i] > tabuleiro[i]:
            return False
    return True

def fazerJogada(jogadas, tabuleiro, vez_computador):
    # Função para efetuar as jogadas no tabuleiro
    for i in range(0, 4):
        tabuleiro[i] -= jogadas[i]

    if vez_computador:
        print("Jogada do computador:", jogadas[0], jogadas[1], jogadas[2], jogadas[3])

def fimDoJogo(tabuleiro):
    # Função para verificar se todas as pilhas do tabuleiro estão vazias
    for jogo in tabuleiro:
        if jogo != 0:
            return False
    return True


# 20 30 0 0

# jogadas = ["20", "30", "0", "0"]
def jogadaHumano(jogador):
    # Função para receber a jogada de um jogador humano

    pergunta = "Jogador " + str(jogador) + "?\nInsira a jogada separada por espaços: "
    jogadas_string = input(pergunta).split()
    
    # ["20", "10", "0", "0"]

    jogadas_int = []

    # String -> Int (convertir)
    for jogada in jogadas_string:
        jogadas_int.append(int(jogada))

    return jogadas_int


def jogadaComputador(tabuleiro):
    # Função para gerar uma jogada aleatória para o computador
    # jogadas = [random.randint(0, x) for x in tabuleiro]

    jogadas = []

    while not validarJogada(jogadas, tabuleiro):
        for pilha in tabuleiro:
            jogadas.append(random.randint(0, pilha))

    return jogadas

def iniciarJogo(opcao):
    # Função para iniciar o jogo com a opção escolhida pelo jogador
    tabuleiro = gerarTabuleiro()
    vez_jogador1 = True
    vez_computador = False

    while not fimDoJogo(tabuleiro):
        # Loop principal do jogo, continua enquanto o jogo não terminar

        mostrarTabuleiro(tabuleiro)

        if vez_jogador1:
            # É a vez do jogador 1 (ou humano, dependendo da opção escolhida)
            jogadas = jogadaHumano(1)
        else:
            # É a vez do jogador 2 (ou computador, dependendo da opção escolhida)
            if opcao == 1:
                jogadas = jogadaHumano(2)
            else:
                jogadas = jogadaComputador(tabuleiro)
                vez_computador = True

        while not validarJogada(jogadas, tabuleiro):
            # Continua pedindo jogadas até que o jogador faça uma jogada válida
            print("Opção inválida!")
            if vez_jogador1:
                jogadas = jogadaHumano(1)
            else:
                jogadas = jogadaHumano(2) if opcao == 1 else jogadaComputador(tabuleiro)

        fazerJogada(jogadas, tabuleiro, vez_computador)
        vez_jogador1 = not vez_jogador1
        vez_computador = False

    # Fim do jogo
    mostrarTabuleiro(tabuleiro)
    if vez_jogador1:
        print("O vencedor foi o jogador 2!" if opcao == 1 else "O vencedor foi o computador!")
    else:
        print("O vencedor foi o jogador 1!")

    menu()

# Inicia o jogo chamando a função menu()
menu()
