# importanto SQLITE
import sqlite3 as lite

# criando conexao com banco de dados.
con = lite.connect('dados.db')

# criando tabelas
with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")
    
