# OPERACOES CRUD

import sqlite3 as lite

# criando conexao 
con = lite.connect('dados.db')

# # Inserir informacoes
# lista =['Herbert Albuquerque','joao@mail.com', 123456789, "12/19/2010", 'Normal', 'Consulta Online']

# CREATE
def inserir_info(i):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ? ,? ,? ,?)"
        cursor.execute(query, i)

# READ
def mostrar_info():
    lista = []
    with con:
        cursor = con.cursor()
        query = "SELECT * FROM formulario"
        cursor.execute(query)
        
        informacao = cursor.fetchall()

        for i in informacao:
            lista.append(i)
    return lista


# UPDATE
def atualizar_info(i):
    with con:
        cursor = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=?  WHERE id=?"
        cursor.execute(query, i)
        

# DELETE
def deletar_info(i):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM formulario WHERE id=? "
        cursor.execute(query, i)

