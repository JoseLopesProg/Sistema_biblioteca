import sqlite3
def inserir_no_banco(titulo, autor, editora, quant):
    conexão = sqlite3.connect('banco.db')
    cursor = conexão.cursor()
    
    sql = 'INSERT INTO livros (Titulo, Autor, Editora, Quantidade) VALUES(?,?,?,?)'
    cursor.execute(sql,(titulo, autor, editora, quant))
    
    conexão.commit()
    conexão.close()


def listar_livros():
    conexão = sqlite3.connect('banco.db')
    cursor = conexão.cursor()
    
    cursor.execute('SELECT * FROM livros')
    livros=cursor.fetchall()#Busca todos os resultados
    
    conexão.close()
    return livros


def excluir_livros(id):
    conexão = sqlite3.connect('banco.db')
    cursor = conexão.cursor()
    
    sql = 'DELETE FROM livros WHERE id = ?'
    cursor.execute(sql,(id,))
    
    #rowcount diz quantas linhas foram afetadas
    if cursor.rowcount > 0:
        print('\033[32mLivro deletado com sucesso!\033[m')
    else:
        print('\033[31mID não encontrado no banco de dados.\033[m')
    
    conexão.commit()
    conexão.close()
    

def editar_livros(id,newTitulo,newAutor,newEditora,newQuantidade):
    conexão = sqlite3.connect('banco.db')
    cursor = conexão.cursor()
    
    sql = """UPDATE livros
            SET Titulo = ?, Autor = ?, Editora = ?, Quantidade = ?
            WHERE id = ?"""
    cursor.execute(sql, (newTitulo, newAutor, newEditora, newQuantidade, id))
    
    conexão.commit()
    conexão.close()
    

def pesquisa_por_nome(termo):
    conexão = sqlite3.connect('banco.db')
    cursor = conexão.cursor()
    # O % antes e depois permite achar o termo em qualquer parte do nome
    cursor.execute('SELECT * FROM livros WHERE Titulo LIKE ?', ('%' + termo + '%',))
    livros = cursor.fetchall() # fetchall porque podem existir vários com o mesmo nome
    conexão.close()
    return livros