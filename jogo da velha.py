import random as rd
import sys
import os
import time as tm
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
matriz = [['1', '2','3','4','5','6','7','8','9']]
lista_robo_jogadas = ['1','2','3','4','5','6','7','8','9']

print(
"""
 _______________________________________
|            JOGO DA VELHA              |
|            1 - Singleplayer           |
|            2 - Multiplayer            |
|            3 - Sair                   |
 ---------------------------------------
 
 
 
 
"""
)
try:
    x = int(input("       Selecione o modo de jogo: "))
    os.system('clear') or None
    while x == 1:
        for linha in matriz:
            a = input("Player escolha um símbolo: ")
            b = input("\n\nPlayer escolha o símbolo do Bot: ")
            lista = [a, b]
            rd.shuffle(lista)
            os.system('clear') or None
            print(linha[0:3])
            print(linha[3:6])
            print(linha[6:9])
            for n in range(4):
                while lista[0] == a:
                    print("\n")
                    z = str(input("Jogador 1 escolha uma casa: "))
                    os.system('clear') or None
                    while z in linha[0:9]:
                        linha.remove(z)
                        linha.insert(int(z)-1, a)
                        lista_robo_jogadas.remove(z)
                        print(linha[0:3])
                        print(linha[3:6])
                        print(linha[6:9])
                        if a in linha[0] and a in linha[1] and a in linha[2] or a in linha[0] and a in                    linha[3] and a in linha[6] or a in linha[1] and a in linha[4] and a in linha[7]                 or a in linha[2] and a in linha[5] and a in linha[8] or a in linha[3] and a in                   linha[4] and a in linha[5] or a in linha[6] and a in linha[7] and a in linha[8]                 or a in linha[0] and a in linha[4] and a in linha[8] or a in linha[2] and a in                   linha[4] and a in linha[6]:
                            print (f"Player ganhou")
                            exit()
                    print("-------Vez do Bot-------")
                    tm.sleep(5)
                    print("\n")
                    rd.shuffle(lista_robo_jogadas)
                    y = lista_robo_jogadas[0]
                    while y in linha[0:9]:
                        linha.remove(y)
                        linha.insert(int(y)-1, b)
                        lista_robo_jogadas.remove(y)
                        os.system('clear') or None
                        print(linha[0:3])
                        print(linha[3:6])
                        print(linha[6:9])
                        if b in linha[0] and b in linha[1] and b in linha[2] or b in linha[0] and b in                    linha[3] and b in linha[6] or b in linha[1] and b in linha[4] and b in linha[7]                 or b in linha[2] and b in linha[5] and b in linha[8] or b in linha[3] and b in                   linha[4] and b in linha[5] or b in linha[6] and b in linha[7] and b in linha[8]                 or b in linha[0] and b in linha[4] and b in linha[8] or b in linha[2] and b in                   linha[4] and b in linha[6]:
                            print (f"Bot ganhou")
                            exit()
                while lista[0] == b:
                    print("-------Vez do Bot-------")
                    tm.sleep(5)
                    print("\n")
                    rd.shuffle(lista_robo_jogadas)
                    y = lista_robo_jogadas[0]
                    while y in linha[0:9]:
                        linha.remove(y)
                        linha.insert(int(y)-1, b)
                        lista_robo_jogadas.remove(y)
                        os.system('clear') or None
                        print(linha[0:3])
                        print(linha[3:6])
                        print(linha[6:9])
                        if b in linha[0] and b in linha[1] and b in linha[2] or b in linha[0] and b in                    linha[3] and b in linha[6] or b in linha[1] and b in linha[4] and b in linha[7]                 or b in linha[2] and b in linha[5] and b in linha[8] or b in linha[3] and b in                   linha[4] and b in linha[5] or b in linha[6] and b in linha[7] and b in linha[8]                 or b in linha[0] and b in linha[4] and b in linha[8] or b in linha[2] and b in                   linha[4] and b in linha[6]:
                            print (f"Bot ganhou")
                            exit()
                        z = str(input("Jogador 1 escolha uma casa: "))
                    os.system('clear') or None
                    while z in linha[0:9]:
                        linha.remove(z)
                        linha.insert(int(z)-1, a)
                        lista_robo_jogadas.remove(z)
                        print(linha[0:3])
                        print(linha[3:6])
                        print(linha[6:9])
                        if a in linha[0] and a in linha[1] and a in linha[2] or a in linha[0] and a in                    linha[3] and a in linha[6] or a in linha[1] and a in linha[4] and a in linha[7]                 or a in linha[2] and a in linha[5] and a in linha[8] or a in linha[3] and a in                   linha[4] and a in linha[5] or a in linha[6] and a in linha[7] and a in linha[8]                 or a in linha[0] and a in linha[4] and a in linha[8] or a in linha[2] and a in                   linha[4] and a in linha[6]:
                            print (f"Player ganhou")
                            exit()
                    print("\n")
            while lista[0] == a:
                z = str(input("Jogador 1 escolha uma casa: "))
                os.system('clear') or None
                while z in linha[0:9]:
                    linha.remove(z)
                    linha.insert(int(z)-1, a)
                    lista_robo_jogadas.remove(z)
                    print(linha[0:3])
                    print(linha[3:6])
                    print(linha[6:9])
                    if a in linha[0] and a in linha[1] and a in linha[2] or a in linha[0] and a in                    linha[3] and a in linha[6] or a in linha[1] and a in linha[4] and a in linha[7]                 or a in linha[2] and a in linha[5] and a in linha[8] or a in linha[3] and a in                   linha[4] and a in linha[5] or a in linha[6] and a in linha[7] and a in linha[8]                 or a in linha[0] and a in linha[4] and a in linha[8] or a in linha[2] and a in                   linha[4] and a in linha[6]:
                        print (f"Player ganhou")
                        exit()
            while lista[0] == b:
                print("-------Vez do Bot-------")
                tm.sleep(5)
                print("\n")
                rd.shuffle(lista_robo_jogadas)
                y = lista_robo_jogadas[0]
                while y in linha[0:9]:
                    linha.remove(y)
                    linha.insert(int(y)-1, b)
                    lista_robo_jogadas.remove(y)
                    os.system('clear') or None
                    print(linha[0:3])
                    print(linha[3:6])
                    print(linha[6:9])
                    if b in linha[0] and b in linha[1] and b in linha[2] or b in linha[0] and b in                    linha[3] and b in linha[6] or b in linha[1] and b in linha[4] and b in linha[7]                 or b in linha[2] and b in linha[5] and b in linha[8] or b in linha[3] and b in                   linha[4] and b in linha[5] or b in linha[6] and b in linha[7] and b in linha[8]                 or b in linha[0] and b in linha[4] and b in linha[8] or b in linha[2] and b in                   linha[4] and b in linha[6]:
                        print (f"Bot ganhou")
                        exit()
    while x == 2:
        for linha in matriz:
            a = input("Jogador 1 escolha um símbolo: ")
            b = input("\n\nJogador 2 escolha um símbolo: ")
            os.system('clear') or None
            print(linha[0:3])
            print(linha[3:6])
            print(linha[6:9])
        for n in range(4):
            print("\n")
            z = str(input("Jogador 1 escolha uma casa: "))
            os.system('clear') or None
            while z in linha[0:9]:
                linha.remove(z)
                linha.insert(int(z)-1, a)
                print(linha[0:3])
                print(linha[3:6])
                print(linha[6:9])
                if a in linha[0] and a in linha[1] and a in linha[2] or a in linha[0] and a in                    linha[3] and a in linha[6] or a in linha[1] and a in linha[4] and a in linha[7]                 or a in linha[2] and a in linha[5] and a in linha[8] or a in linha[3] and a in                   linha[4] and a in linha[5] or a in linha[6] and a in linha[7] and a in                               linha[8] or a in linha[0] and a in linha[4] and a in linha[8] or a in linha[2]                    and a in linha[4] and a in linha[6]:
                    print (f"Jogador 1 ganhou")
                    exit()
            print("\n")
            y = str(input("Jogador 2 escolha uma casa: "))
            while y in linha[0:9]:
                linha.remove(y)
                linha.insert(int(y)-1, b)
                os.system('clear') or None
                print(linha[0:3])
                print(linha[3:6])
                print(linha[6:9])
                if b in linha[0] and b in linha[1] and b in linha[2] or b in linha[0] and b in                    linha[3] and b in linha[6] or b in linha[1] and b in linha[4] and b in linha[7]                 or b in linha[2] and b in linha[5] and b in linha[8] or b in linha[3] and b in                   linha[4] and b in linha[5] or b in linha[6] and b in linha[7] and b in linha[8]                 or b in linha[0] and b in linha[4] and b in linha[8] or b in linha[2] and b in                        linha[4] and b in linha[6]:
                    print (f"Jogador 2 ganhou")
        print("\n")
        z = str(input("Jogador 1 escolha uma casa: "))
        os.system('clear') or None
        linha.remove(z)
        linha.insert(int(z)-1, a)
        print(linha[0:3])
        print(linha[3:6])
        print(linha[6:9])
        if a in linha[0] and a in linha[1] and a in linha[2] or a in linha[0] and a in                    linha[3] and a in linha[6] or a in linha[1] and a in linha[4] and a in linha[7]                 or a in linha[2] and a in linha[5] and a in linha[8] or a in linha[3] and a in                   linha[4] and a in linha[5] or a in linha[6] and a in linha[7] and a in                               linha[8] or a in linha[0] and a in linha[4] and a in linha[8] or a in linha[2]                    and a in linha[4] and a in linha[6]:
                    print (f"Jogador 1 ganhou")
                    exit()
        print("Jogo Empatado")
        input("Pressione enter para continuar jogando.....")
        os.system('clear') or None
        restart_program()
    while x == 3:
        print("Encerrando o jogo....")
        break
except ValueError:
    os.system('clear') or None
    print("MODO DE JOGO INCORRETO")
    print("      FECHANDO...")
