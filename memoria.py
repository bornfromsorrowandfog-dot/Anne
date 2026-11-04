import sqlite3

class Memoria:

    def __init__(self, caminho="banco.db"):

        self.conexao = sqlite3.connect(caminho)

        self.cursor = self.conexao.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT,
            resposta TEXT
        )
        """)

        self.conexao.commit()

    def salvar(self, pergunta, resposta):

        self.cursor.execute(
            "INSERT INTO memoria (pergunta, resposta) VALUES (?, ?)",
            (pergunta, resposta)
        )

        self.conexao.commit()

    def pesquisar(self, pergunta):

        self.cursor.execute(
            "SELECT resposta FROM memoria WHERE pergunta = ?",
            (pergunta,)
        )

        resultado = self.cursor.fetchone()

        if resultado:
            return resultado[0]

        return None