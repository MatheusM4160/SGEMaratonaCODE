import json
import sqlite3


db = r"app/db/db_fornecedores.json"



class Fornecedores:
    def __init__(self):
        pass
    
    def salvar(self,fornecedores):
        with open(db, "w", encoding="utf-8") as file:
            json.dump(fornecedores, file, indent=4, ensure_ascii=False)

    def ler(self):    
        with open(db, 'r') as file:
            db = json.load(file)
            file.close()

        return db

db = r"app/db/db.sqlite"

class FornecedoresDB:
    def __init__(self):
        pass

    def ler(self):
        def fetch_all_as_dict(cursor):
            colunas = [col[0] for col in cursor.description]
            return [dict(zip(colunas, row)) for row in cursor.fetchall()]
        
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            cursor.execute("""SELECT * FROM fornecedores""")
            resultado = fetch_all_as_dict(cursor)
            return resultado
        
    def inserir(self, nome_fornecedor, nome_produto, numero_de_contato):
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            cursor.execute("""INSERT INTO fornecedores (nome_fornecedor, nome_produto, numero_de_contato)
                        VALUES (?, ?, ?)""", (nome_fornecedor, nome_produto, numero_de_contato))
            con.commit()

    def excluir_fornecedor(self, id):
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            cursor.execute("""DELETE FROM fornecedores WHERE id = ?""", (id,))
            con.commit()