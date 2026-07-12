from time import sleep
import os
from funções import *
import sqlite3

conexão = sqlite3.connect('banco.db')
cursor = conexão.cursor()

#Criação da Tabela
cursor.execute("""CREATE TABLE IF NOT EXISTS contas_bancárias (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Autor TEXT NOT NULL,
    Editora TEXT NOT NULL,
    Quantidade INTEGER
    )""")

#Solicitar dados ao usuário
cabeçalho('SISTEMA BIBLIOTECA')

resp=menu(['Cadastrar livros','Excluir livros', 'Editar livros','Pesquisar','Ver lista de livros', 'Sair do sistema'])

match resp:
    case 1:
        cabeçalho('Cadastrar livros')
        sleep(2)
        os.system('cls')
    case 2:
        cabeçalho('Excluir livros')
        sleep(2)
        os.system('cls')
    case 3:
        cabeçalho('Editar Livros')
        sleep(2)
        os.system('cls')
    case 4:
        cabeçalho('Pesquisar')
        sleep(2)
        os.system('cls')
    case 5:
        cabeçalho('Ver lista de livros')
        sleep(2)
        os.system('cls')
    case _:
        cabeçalho('Saindo do sistema... Até logo!')


conexão.commit()