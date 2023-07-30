"""
Trabalho final - jogo NIM

1 - Menu com opções

2 - Gerar tabuleiro aleatorio

3 - Solicitar a jogada ao jogador

4 - Validar jogada

5 - Se valido, mostrar o tabuleiro atualizado + solicitar jogada ao jogador 2
 se não: Mostrar mensagem "opção invalida" e solicitar novamente a jogada ao jogador 1

"""
import random

# Gerar tabuleiro inicial
tabuleiro = list()
def menu():
    global tabuleiro
    print("""
0 - Sair
1 - Humano vs Humano
2 - Humano vs Computador
    """)

    # Gerar tabuleiro com numeros aleatorios
    tabuleiro = [random.randint(1, 30), random.randint(1, 30), random.randint(1, 30),
                              random.randint(1, 30)]



    # Validar jogadas
    opcao = -1
    while 0 > opcao or opcao > 2:
        opcao = int(input("Opção:"))
# Iniciando jogo
    if opcao == 1 or opcao == 2:
        iniciarGame(opcao)
# Saindo do jogo
    elif opcao == 0:
        print("Obrigado por jogar o meu jogo!")

# Verificar se a jogada é valida: verificando se os valores são menores que o do tabuleiro e não são valores negativos
def verificarJogada(p1, p2, p3, p4):
    jogadas = [p1, p2, p3, p4]
    x = jogadas.count(0)

    if 1 > x > 3:
        return False

    elif  p1 < 0 or p1 > tabuleiro[0]:
        return False

    elif p2 < 0 or p2 > tabuleiro[1]:
        return False
    elif p3 < 0 or p3 > tabuleiro[2]:
        return False
    elif p4 < 0 or p4 > tabuleiro[3]:
        return False
    else:
        return True

def fazerJogada(p1, p2, p3, p4):
    # Criar lista com as jogadas do parametro
    jogadas = [p1, p2, p3, p4]

    for i in range(0, 4):
        tabuleiro[i] -= jogadas[i]

def iniciarGame(opcao):
    vezJogador1 = True
    fim = False

    # Opção HUMANO vs HUMANO
    if opcao == 1:
        # Enquanto não acabar o jogo, faça o loop:
        while not fim:
            # Mostrar o tabuleiro
            print("Tabuleiro:", tabuleiro[0], tabuleiro[1], tabuleiro[2], tabuleiro[3])

            # Se for vez do jogador 1, faça isso:
            if vezJogador1:
                #Pedir a jogada ao jogador, e armazenar cada valor em uma variavel
                p1, p2, p3, p4 = eval(input("Jogador 1?\nInsere a jogada\n"))

                # Verificar se a jogada foi valida
                jogadaValida = verificarJogada(p1, p2, p3, p4)

                # Se a jogada não for valida, faça isso:
                if not jogadaValida:
                    # Enquanto a jogada não for valida, faça isso:
                    while not jogadaValida:
                        print("Opção invalida!")
                        # Pedir novamente a jogada
                        p1, p2, p3, p4 = eval(input("Jogador 1?\nInsere a jogada\n"))
                        # Verificar novamente se a jogada foi valida
                        jogadaValida = verificarJogada(p1, p2, p3, p4)

                # Efetuar a jogada:
                fazerJogada(p1, p2, p3, p4)

                # Se todos os valores do tabuleiro são 0, fim do jogo
                if tabuleiro.count(0) == 4:
                    # Definir a variavel FIM como True
                    fim = True

                    if vezJogador1:
                        print("O vencedor foi o jogador 1!")
                    else:
                        print("O vencedor foi o jogador 2!")
                # Passar a vez para o jogador 2, Definir a vez do jogador 1 como False
                vezJogador1 = False

            # opção HUMANO vs COMPUTADOR
            else:

                #Pedir a jogada ao jogador, e armazenar cada valor em uma variavel
                p1, p2, p3, p4 = eval(input("Jogador 2?\nInsere a jogada\n"))

                # Verificar se a jogada foi valida
                jogadaValida = verificarJogada(p1, p2, p3, p4)

                if not jogadaValida:
                    while not jogadaValida:
                        print("Opção invalida!")
                        p1, p2, p3, p4 = eval(input("Jogador 2?\nInsere a jogada\n"))
                        jogadaValida = verificarJogada(p1, p2, p3, p4)

                fazerJogada(p1, p2, p3, p4)
                if tabuleiro.count(0) == 4:
                    fim = True
                    if vezJogador1:
                        print("O vencedor foi o jogador 1!")
                    else:
                        print("O vencedor foi o jogador 2!")
                vezJogador1 = True

    else:
        while not fim:
            print("Tabuleiro:", tabuleiro[0], tabuleiro[1], tabuleiro[2], tabuleiro[3])

            if vezJogador1:
                p1, p2, p3, p4 = eval(input("Jogador 1?\nInsere a jogada\n"))
                jogadaValida = verificarJogada(p1, p2, p3, p4)
                if not jogadaValida:
                    while not jogadaValida:
                        print("Opção invalida!")
                        p1, p2, p3, p4 = eval(input("Jogador 1?\nInsere a jogada\n"))
                        jogadaValida = verificarJogada(p1, p2, p3, p4)

                fazerJogada(p1, p2, p3, p4)
                if tabuleiro.count(0) == 4:
                    fim = True
                    if vezJogador1:
                        print("O vencedor foi o jogador 1!")
                    else:
                        print("O vencedor foi o jogador 2!")

                vezJogador1 = False

            else:
                jogadas = [0, 0, 0, 0]

                while not 1 < jogadas.count(0) < 4:
                    jogadas = [
                        random.randint(0,tabuleiro[0]),
                        random.randint(0,tabuleiro[1]),
                        random.randint(0,tabuleiro[2]),
                        random.randint(0,tabuleiro[3])
                    ]

                print("Computador: \n", jogadas[0], jogadas[1], jogadas[2], jogadas[3])

                fazerJogada(jogadas[0], jogadas[1], jogadas[2], jogadas[3])

                if tabuleiro.count(0) == 4:
                    fim = True
                    if vezJogador1:
                        print("O vencedor foi o jogador 1!")
                    else:
                        print("O vencedor foi o computador!")
                vezJogador1 = True

    menu()


menu()




