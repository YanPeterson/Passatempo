import sqlite3

import PySimpleGUI as psg
import sqlite3 as sql
import os

diretorio_corrente = os.path.dirname(os.path.abspath(__file__))
dbpath = os.path.join(diretorio_corrente, 'Alunos_Cadastrados.db')
conexao = sql.connect(dbpath)
cr = conexao.cursor()


cr.execute("CREATE TABLE IF NOT EXISTS OPCOES('Nome do Aluno', 'Número da CRE', 'Escola do Aluno')")
cr.execute("CREATE TABLE IF NOT EXISTS INGRESSOS ('Ingressos')")

opcoes = ['Nome do Aluno', 'Número da CRE', 'Escola do Aluno']
ingressos = ['']

layout = [[psg.Text('Número da CRE'), psg.Input(size=2, key=opcoes[1])],
         [psg.Text('Nome do Aluno'), psg.Input(size=50, key=opcoes[0])],
         [psg.Text('Escola do aluno'), psg.Input(size=40, key=opcoes[2])], [psg.Button('Adicionar Aluno')],
         [psg.Exit('Sair'), psg.Button('Adicionar ingressos'), psg.Input(size=5, key=ingressos[0])]]

window = psg.Window('Cadastro', layout)

while True:
    event, values = window.read()
    print(values)

    if event == psg.WIN_CLOSED or event == 'Sair':  # if user closes window or clicks cancel
        break

    if event == 'Adicionar ingressos':
        ingressos.append(values[ingressos[0]])
        conexao = sqlite3.connect(dbpath)
        conexao.execute("INSERT INTO INGRESSOS (Ingressos) VALUES (?) ", [values[ingressos[0]]])
        conexao.commit()
        conexao.close()
    if event == 'Adicionar Aluno':
        ingressos.append(values[ingressos[0]])
        conexao = sqlite3.connect(dbpath)
        conexao.execute("INSERT INTO OPCOES ('Nome do Aluno', 'Número da CRE', 'Escola do Aluno') VALUES (?, ?, ?) ",
                        ([values[opcoes[0]], values[opcoes[1]],values[opcoes[2]]]))
        conexao.commit()
        conexao.close()
