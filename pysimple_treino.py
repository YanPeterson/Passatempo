import PySimpleGUI as psg

import sqlite3
import os

diretorio_corrente = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(diretorio_corrente, 'database.db')

conexao = sqlite3.connect(db_path)
query = (''' CREATE TABLE IF NOT EXISTS SUPLEMENTO (LOTE CHAR(10), PRODUTO TEXT, FORNECEDOR TEXT)''')
conexao.execute(query)
conexao.close()

dados = []
Titulos = ['Lote', 'Produto', 'Fornecedor']

layout = [
        [psg.Text(Titulos[0]), psg.Input(size=5, key=Titulos[0])],
        [psg.Text(Titulos[1]), psg.Input(size=20, key=Titulos[1])],
        [psg.Text(Titulos[2]), psg.Combo(['Fornecedor 1', 'Fornecedor 2', 'Fornecedor 3'], key=Titulos[2])],
        [psg.Button('Adicionar'), psg.Button('Salvar', disabled=True), psg.Button('Editar'),psg.Button('Excluir'), psg.Exit('Sair')],
        [psg.Table(dados, Titulos, key='tabela')]
]

window = psg.Window('Sistema de gerencia de suplementos', layout)

while True:

    event, values = window.read()
    print(values)

    if event == 'Adicionar':
        dados.append([values[Titulos[0]],values[Titulos[1]],values[Titulos[2]]])
        window['tabela'].update(values=dados)
        for i in range(3):
            window[Titulos[i]].update(value='')

        conexao = sqlite3.connect(db_path)
        conexao.execute("INSERT INTO SUPLEMENTO (LOTE, PRODUTO, FORNECEDOR) VALUES (?, ?, ?) ", ([values[Titulos[0]],values[Titulos[1]],values[Titulos[2]]]))
        conexao.commit()
        conexao.close()

    if event == 'Editar':
        if values['tabela'] ==[]:
            psg.popup('Nenhuma linha selecionada')
        else:
            editarLinha=values['tabela'][0]
            for i in range(3):
                window[Titulos[i]].update(value=dados[editarLinha][i])
            window['Salvar'].update(disabled=False)

    if event == 'Salvar':
        dados[editarLinha] =[values[Titulos[0]], values[Titulos[1]],values[Titulos[2]]]
        window['tabela'].update(values=dados)
        for i in range(3):
            window[Titulos[i]].update(value='')
        window['Salvar'].update(disabled=True)

    conexao = sqlite3.connect(db_path)
    conexao.execute('UPDATE SUPLEMENTO set PRODUTO = ?, FORNECEDOR = ? where LOTE = ?' ,([values[Titulos[1]], values[Titulos[2]], values[Titulos[0]]]))
    conexao.commit()
    conexao.close()

    if event == 'Excluir':
        if values['tabela']==[]:
            psg.popup('Nenhuma linha selecionada')
        else:
            if psg.popup_ok_cancel('Essa operação não pode ser desfeita. Confirma?') == 'OK':

                conexao = sqlite3.connect(db_path)
                conexao.execute('DELETE FROM SUPLEMENTO WHERE LOTE = ?;', (values[Titulos[0]],))
                conexao.close()

                del dados[values['tabela'][0]] #Remove linha selecionada
                window['tabela'].update(values=dados)

    if event in (psg.WIN_CLOSED, 'Sair'):
        break

window.close()


