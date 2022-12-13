"""
Jogo de perguntas e respostas para treinar Python

"""
import random
from random import shuffle
from os import system
lista1 = ['Quanto é 1x2', 'Quanto é 5+1', 'Quanto é 3x3', 'Quanto é 25/5']
random.shuffle(lista1)
lista2 = ['2', '6', '9', '5']
res = ['13', '10', '15', '3', '7', '4', '1', '8']
random.shuffle(res)
op0 = lista2[0]
op1 = lista2[1]
op2 = lista2[2]
op3 = lista2[3]
pont = 0

print("""--------------- Jogo do Quiz ---------------

1- Começar o jogo 
2- Continuar jogo
3- Parar jogo
""")
opcao = input('Selecione a opção que deseja: ')
system('cls')
while opcao == '1':
    print("""--------------- O jogo começou --------------- 
    """)
    break
while opcao == '3':
    print('Encerrando o jogo')
    quit()
x = [f"""
a) {lista2[0]}
b) {res[1]}
c) {res[2]}
d) {res[0]}
""", f"""
a) {res[0]}
b) {lista2[0]}
c) {res[2]}
d) {res[1]}
""", f"""
a) {res[0]}
b) {res[1]}
c) {lista2[0]}
d) {res[2]}

""", f"""
a) {res[0]}
b) {res[1]}
c) {res[2]}
d) {lista2[0]}
"""]
random.shuffle(x)

y = [f"""
a) {lista2[1]}
b) {res[1]}
c) {res[2]}
d) {res[0]}
""", f"""
a) {res[0]}
b) {lista2[1]}
c) {res[2]}
d) {res[1]}
""", f"""
a) {res[0]}
b) {res[1]}
c) {lista2[1]}
d) {res[2]}

""", f"""
a) {res[0]}
b) {res[1]}
c) {res[2]}
d) {lista2[1]}
"""]
random.shuffle(y)


z = [f"""
a) {lista2[2]}
b) {res[1]}
c) {res[2]}
d) {res[0]}
""", f"""
a) {res[0]}
b) {lista2[2]}
c) {res[2]}
d) {res[1]}
""", f"""
a) {res[0]}
b) {res[1]}
c) {lista2[2]}
d) {res[2]}

""", f"""
a) {res[0]}
b) {res[1]}
c) {res[2]}
d) {lista2[2]}
"""]
random.shuffle(z)

z1 = [f"""
a) {lista2[3]}
b) {res[1]}
c) {res[2]}
d) {res[0]}
""", f"""
a) {res[0]}
b) {lista2[3]}
c) {res[2]}
d) {res[1]}
""", f"""
a) {res[0]}
b) {res[1]}
c) {lista2[3]}
d) {res[2]}

""", f"""
a) {res[0]}
b) {res[1]}
c) {res[2]}
d) {lista2[3]}
"""]
random.shuffle(z1)


while lista1[0] == 'Quanto é 1x2':
    print("""Quanto é 1x2
    """)
    print (f'{x[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op0:
    pont = pont + 10
    break
while lista1[0] == 'Quanto é 5+1':
    print("""Quanto é 5+1
    """)
    print(f'{y[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op1:
    pont = pont + 10
    break
while lista1[0] == 'Quanto é 3x3':
    print("""Quanto é 3x3
    """)
    print(f'{z[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op2:
    pont = pont + 10
    break
while lista1[0] == 'Quanto é 25/5':
        print("""Quanto é 25/5
        """)
        print(f'{z1[0]}')
        res = input('Qual é a resposta? ')
        break
while res == op3:
        pont = pont + 10
        break

while lista1[1] == 'Quanto é 1x2':
    print("""Quanto é 1x2
    """)
    print (f'{x[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op0:
    pont = pont + 10
    break
while lista1[1] == 'Quanto é 5+1':
    print("""Quanto é 5+1
    """)
    print(f'{y[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op1:
    pont = pont + 10
    break
while lista1[1] == 'Quanto é 3x3':
    print("""Quanto é 3x3
    """)
    print(f'{z[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op2:
    pont = pont + 10
    break
while lista1[1] == 'Quanto é 25/5':
        print("""Quanto é 25/5
        """)
        print(f'{z1[0]}')
        res = input('Qual é a resposta? ')
        break
while res == op3:
        pont = pont + 10
        break

while lista1[2] == 'Quanto é 1x2':
    print("""Quanto é 1x2
    """)
    print (f'{x[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op0:
    pont = pont + 10
    break
while lista1[2] == 'Quanto é 5+1':
    print("""Quanto é 5+1
    """)
    print(f'{y[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op1:
    pont = pont + 10
    break
while lista1[2] == 'Quanto é 3x3':
    print("""Quanto é 3x3
    """)
    print(f'{z[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op2:
    pont = pont + 10
    break
while lista1[2] == 'Quanto é 25/5':
        print("""Quanto é 25/5
        """)
        print(f'{z1[0]}')
        res = input('Qual é a resposta? ')
        break
while res == op3:
        pont = pont + 10
        break

while lista1[3] == 'Quanto é 1x2':
    print("""Quanto é 1x2
    """)
    print (f'{x[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op0:
    pont = pont + 10
    break
while lista1[3] == 'Quanto é 5+1':
    print("""Quanto é 5+1
    """)
    print(f'{y[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op1:
    pont = pont + 10
    break
while lista1[3] == 'Quanto é 3x3':
    print("""Quanto é 3x3
    """)
    print(f'{z[0]}')
    res = input('Qual é a resposta? ')
    break
while res == op2:
    pont = pont + 10
    break
while lista1[3] == 'Quanto é 25/5':
        print("""Quanto é 25/5
        """)
        print(f'{z1[0]}')
        res = input('Qual é a resposta? ')
        break
while res == op3:
        pont = pont + 10
        break