import sqlite3

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

    def alterar_fornecedor(self, id, nome_fornecedor=None, nome_produto=None, numero_de_contato=None):
        with sqlite3.connect(db) as con:
            cursor = con.cursor()
            cursor.execute("""SELECT nome_forncedor, nome_produto, numero_de_contato FROM fornecedores WHERE id=?""", (id,))
            resultado = cursor.fetchone()

            if resultado:
                nome_forncedor_atual, nome_produto_atual, numero_de_contato_atual = resultado
                novo_nome_forncedor = nome_fornecedor if nome_fornecedor is not None else nome_forncedor_atual
                novo_nome_produto = nome_produto if nome_produto is not None else nome_produto_atual
                novo_numero_de_contato = numero_de_contato if numero_de_contato is not None else numero_de_contato_atual

                cursor.execute("""UPDATE fornecedores
                               SET nome_fornecedor = ?,
                               nome_produto = ?,
                               numero_de_contato = ?
                               WHERE id=?
                               """, (novo_nome_forncedor, novo_nome_produto, novo_numero_de_contato, id))

                con.commit()