import random as rd
qtd_senha = int(input("Insira quantas senhas deseja gerar: "))
x = 1
cad_caract = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lista_senha = []
lista2 = []
while x <= qtd_senha:
    y = 1
    caracters = int(input("Quantos caracters dejesa nessa senha: "))
    while y <= caracters:
        z = rd.randrange(0, 46)
        lista2.append(str(cad_caract[z]))
        y = y + 1
    senha = ''.join(lista2)
    lista_senha.append(senha)
    x = x + 1
    y = 1
    lista2 = []
print(lista_senha)
