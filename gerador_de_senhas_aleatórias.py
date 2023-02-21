import random as rd
qtd_senha = int(input("Insira quantas senhas deseja gerar: "))
x = 1
y = 1
lista_senha = [ ]
lista2 = []
while x <= qtd_senha:
    caracters = int(input("Quantos caracters dejesa nessa senha: "))
    while y <= caracters:
        z = rd.randrange(0, 10)
        lista2.append(str(z))
        y = y + 1
    senha = ''.join(lista2)
    lista_senha.append(senha)
    x = x + 1
    y = 1
    lista2 = []
print(lista_senha)
    