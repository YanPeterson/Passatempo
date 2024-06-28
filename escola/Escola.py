import escola_arquivos
from escola_arquivos import Aluno, Professor

#Utilizando um banco de dados
import os
import sqlite3 as sql

diretorio_corrente = os.path.dirname(os.path.abspath(__file__))
dbpath = os.path.join(diretorio_corrente, 'Alunos_Cadastrados2.db')
conexao = sql.connect(dbpath)  #Alunos_Cadastrados2.db
conexao.execute("CREATE TABLE IF NOT EXISTS Aluno('nome', 'matricula', 'cpf')")

dados_aluno = []

aluno1 = Aluno(input("Digite o nome: "),input("Digite o matricula: "),input("Digite o cpf: "))
dados_aluno.append(aluno1.nome)
dados_aluno.append(aluno1.matricula)
dados_aluno.append(aluno1.cpf)

print(dados_aluno)

conexao.execute("INSERT INTO Aluno ('nome', 'matricula', 'cpf') VALUES(?, ?, ?)",
                (dados_aluno[0], dados_aluno[1], dados_aluno[2]))
conexao.commit()
conexao.close()