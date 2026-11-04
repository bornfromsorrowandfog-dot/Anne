from personalidade import Personalidade
from aprendizado import Aprendizado
from matematica import calcular

class Cerebro:

    def __init__(self, memoria):

        self.personalidade = Personalidade()

        self.aprendizado = Aprendizado(memoria)

    def pensar(self, mensagem):

        mensagem = mensagem.lower().strip()

        if mensagem == "olá":
            return "Olá! Como posso ajudar?"

        if mensagem == "quem é você?":
            return self.personalidade.apresentar()

        if mensagem.startswith("calcular "):

            expressao = mensagem.replace(
                "calcular ", "", 1
            )

            return calcular(expressao)

        resposta = self.aprendizado.consultar(mensagem)

        if resposta:
            return resposta

            return None