from time import sleep
import os
from funções import *
import sqlite3
from dados import *

conexão = sqlite3.connect('banco.db')
cursor = conexão.cursor()

#Criação da Tabela
cursor.execute("""CREATE TABLE IF NOT EXISTS livros (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Titulo TEXT NOT NULL,
    Autor TEXT NOT NULL,
    Editora TEXT NOT NULL,
    Quantidade INTEGER
    )""")

while True:
    cabeçalho('SISTEMA BIBLIOTECA')
    #SOLICITANDO OS DADOS AO USUÁRIO
    resp=menu(['Cadastrar livros','Excluir livros', 'Editar livros','Pesquisar','Ver lista de livros', 'Sair do sistema'])
    match resp:
        case 1:
            #CADASTRO DOS LIVROS
            cadastrar()
            os.system('cls')
        case 2:
            #DELETAR LIVROS CADASTRADOS
            excluir()
            os.system('cls')
        case 3:
            #ATUALIZANDO LIVROS CADASTRADOS
            editar()
            os.system('cls')
        case 4:
            #PESQUISA DE LIVROS CADASTRADOS
            pesquisa()
            os.system('cls')
        case 5:
            #LISTAR TODOS OS LIVROS CADASTRADOS
            cabeçalho('Ver lista de livros')
            lista = listar_livros()
            for livro in lista:
                print(f'ID: {livro[0]} | Titulo: {livro[1]} | Autor: {livro[2]} | Editora: {livro[3]} | Quantidade: {livro[4]}')
            input('\nPressione ENTER para voltar ao menu...')
            os.system('cls')
        case _:
            cabeçalho('Saindo do sistema... Até logo!')
            break

print('Obrigado por ultilizar o programa!')