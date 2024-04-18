import os

print('*********************************')
print('** Bem vindo a palavra secreta **')
print('*********************************')
dif = 1
print(""" 1- Jogar
 2- Sair
 3- Opções""")
print("""                                                      Dificuldade atual = 1""")
op = int(input("\nEscolha a opção desejada: "))
palavra_secreta = 'banana'
os.system('cls') or None
if op == 1:
    x = 1
    tent = 10
    print('*********************************')
    print('********Bem vindo ao jogo *******')
    print('*********************************')
    print(f"\nA primeira dica é:\n\nA palavra secreta é uma fruta")
    for i in range(10):
        print(f"Você possui {tent} tentativas")
        a = str(input(f"Tentativa número {x}: "))
        a = a.lower()
        if a == palavra_secreta:
            print("Parabéns você acertou")
            exit()
        else:
            print('Resposta errada!!!\n')
            x = x + 1
            tent = tent - 1
        if i == 9:
            print("Você esgotou suas tentativas Game OVER!!!")
    print('Fim do jogo')
if op == 2:
    print('Fechando app ...')
    exit()
if op == 3:
    dif = int(input("\nSelecione a dificuldade do jogo: "))
    x = 1
    print('*********************************')
    print('********Bem vindo ao jogo *******')
    print('*********************************')
    print(f"\nA dica é:\n\nA palavra secreta é uma fruta")
    if dif == 1:
        tent = 10
        for i in range(10):
            print(f"Você possui {tent} tentativas")
            a = str(input(f"Tentativa número {x}: "))
            a = a.lower()
            if a == palavra_secreta:
                print("Parabéns você acertou")
                exit()
            else:
                print('Resposta errada!!!\n')
                x = x + 1
                tent = tent - 1
            if i == 9:
                print("Você esgotou suas tentativas Game OVER!!!")
        print('Fim do jogo')
    if dif == 2:
        tent = 8
        for i in range(8):
            print(f"Você possui {tent} tentativas")
            a = str(input(f"Tentativa número {x}: "))
            a = a.lower()
            if a == palavra_secreta:
                print("Parabéns você acertou")
                exit()
            else:
                print('Resposta errada!!!\n')
                x = x + 1
                tent = tent - 1
            if i == 7:
                print("Você esgotou suas tentativas Game OVER!!!")
        print('Fim do jogo')
    if dif == 3:
        tent = 5
        for i in range(5):
            print(f"Você possui {tent} tentativas")
            a = str(input(f"Tentativa número {x}: "))
            a = a.lower()
            if a == palavra_secreta:
                print("Parabéns você acertou")
                exit()
            else:
                print('Resposta errada!!!\n')
                x = x + 1
                tent = tent - 1
            if i == 4:
                print("Você esgotou suas tentativas Game OVER!!!")
        print('Fim do jogo')
    if dif == 4:
        tent = 3
        for i in range(3):
            print(f"Você possui {tent} tentativas")
            a = str(input(f"Tentativa número {x}: "))
            a = a.lower()
            if a == palavra_secreta:
                print("Parabéns você acertou")
                exit()
            else:
                print('Resposta errada!!!\n')
                x = x + 1
                tent = tent - 1
            if i == 2:
                print("Você esgotou suas tentativas Game OVER!!!")
        print('Fim do jogo')
