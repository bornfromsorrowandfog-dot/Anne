class Personalidade:

    def __init__(self):
        self.nome = "A.N.N.E."
        self.versao = "0.1 Alpha"
        self.criadora = "Daniel"

    def apresentar(self):
        return (
            f"Olá! Eu sou {self.nome}.\n"
            f"Versão: {self.versao}\n"
            "Estou iniciando meus sistemas."
        )