from dados import *
def linha(tam=35):
    return print('-'*tam)


def cabeçalho(txt):
    linha()
    print(txt.center(35))
    linha()
    

def menu(lista):
    c=1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    linha()
    opc = leiaInt('Escolha uma opção: ')
    return opc


def leiaInt(msg):
    while True:
        try:
            resp = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            if resp < 7 and resp > 0:
                return resp
            else:
                print('\033[31mERRO: por favor, digite uma opção válida.\033[m')
                

def cadastrar():
    while True:
        cabeçalho('Cadastro de livros')
        titulo = input('Digite o título do livro: ')
        autor = input('Digite o nome do autor: ')
        editora = input('Digite a editora: ')
        quant = int(input('Digite a quantidade: '))
        
        #Chama a função do arquivo dados.py
        inserir_no_banco(titulo, autor, editora, quant)
        print('Livro cadastrado com sucesso!')
        resp = input('Deseja cadastrar outro livro [S/N]? ').upper().strip()
        if resp in 'Ss':
            continue
        else:
            break


def excluir():
    while True:
        cabeçalho('Deletar Livro')
        id=int(input('Digite o ID para excluir: '))
        
        #chama a função do arquivo dados.py
        excluir_livros(id)
        resp = input('Deseja deletar outro livro [S/N]? ').upper().strip()
        if resp in 'Ss':
            continue
        else:
            break


def editar():
    while True:
        cabeçalho('Atualizar registros')
        id = int(input('Digite o ID do livro que deseja atualizar: '))
        #coletando os novos dados
        print('Digite os novos dados: ')
        titulo = input('Novo titulo: ')
        autor = input('Novo autor: ')
        editora = input('Nova editora: ')
        str_quantidade = input('Nova quantidade: ')
        if str_quantidade == '':
            quantidade = 0
        else:
            quantidade = int(str_quantidade)

        #chama a função com os novos valores.
        editar_livros(id, titulo, autor, editora, quantidade)
        print('\033[32mLivro atualizado com sucesso!\033[m')
        resp = input('Deseja atualizar outro livro [S/N]? ').upper().strip()
        if resp in 'Ss':
            continue
        else:
            break
        
        
def pesquisa():
    while True:
        cabeçalho('Pesquisa de livros...')
        termo = input('Digite uma palavra chave para buscar o livro: ')
        lista_livros = pesquisa_por_nome(termo)
        
        if lista_livros:
            print(f'\nForam encontrados {len(lista_livros)} resultado(s):')
            for livro in lista_livros:
                # livro aqui é uma tupla: (id, titulo, autor, editora, quantidade)
                print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Editora: {livro[3]} | Qtd: {livro[4]}")
        else:
            print('\033[31mAviso: Nenhum livro encontrado com esse termo.\033[m')
            
        resp = input('\nDeseja pesquisar outro livro [S/N]? ').upper().strip()
        if resp in 'Ss':
            continue
        else:
            break