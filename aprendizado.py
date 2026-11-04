class Aprendizado:

    def __init__(self, memoria):
        self.memoria = memoria

    def aprender(self, pergunta, resposta):

        self.memoria.salvar(
            pergunta.lower().strip(),
            resposta
        )

        return "Informação armazenada com sucesso!"

    def consultar(self, pergunta):

        return self.memoria.pesquisar(
            pergunta.lower().strip()
        )