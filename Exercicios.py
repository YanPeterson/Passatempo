"""

Arquivo para treinar Python

1)Usually when you buy something, you're asked whether your credit card number, phone number
or answer to your most secret question is still correct. However, since someone could look over your shoulder,
 you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into #

Exemplos: "123761838746" >>>> "12376****746"
"""

def Convert(string):
    cpf1 = []
    cpf1[:0]=string
    return cpf1
cpf2 = input('Insira seu cpf: ')
cpf2 = (Convert(cpf2))

cpf2.pop(0)
cpf2.insert(0, '*')

cpf2.pop(1)
cpf2.insert(1, '*')

cpf2.pop(2)
cpf2.insert(2, '*')

cpf2.pop(6)
cpf2.insert(6, '*')

cpf2.pop(7)
cpf2.insert(7, '*')

cpf2.pop(8)
cpf2.insert(8, '*')

strcpf = ''.join(cpf2)
print(F'Seu cpf é: {strcpf}')
