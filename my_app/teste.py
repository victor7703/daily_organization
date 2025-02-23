import sqlite3
from . import db
from . import create_app

app = create_app()

with app.app_context():
    

    conexao = db.get_db()

    cursor = conexao.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")

    dados = cursor.fetchall()

    print(dict(dados[0]))  

#Verificando se a tabela foi criada no banco de dados.