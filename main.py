import traceback
try:
    # todo o seu código atual do app aqui
    pass
except Exception:
    erro = traceback.format_exc()
    from kivy.app import App
    from kivy.uix.label import Label
    class ErroApp(App):
        def build(self):
            return Label(text=erro, text_size=(900, None))
    ErroApp().run()
import os
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from memoria import Memoria
from cerebro import Cerebro

Window.softinput_mode = "below_target"


class AnneApp(App):

    def build(self):
        self.title = "A.N.N.E."
        caminho = os.path.join(self.user_data_dir, "banco.db")
        self.memoria = Memoria(caminho)
        self.anne = Cerebro(self.memoria)
        self.pendente = None

        raiz = BoxLayout(orientation="vertical", padding=8, spacing=8)

        self.scroll = ScrollView()
        self.chat = Label(
            text="", size_hint_y=None,
            halign="left", valign="top"
        )
        self.chat.bind(
            width=lambda i, w: setattr(i, "text_size", (w, None)),
            texture_size=lambda i, s: setattr(i, "height", s[1])
        )
        self.scroll.add_widget(self.chat)
        raiz.add_widget(self.scroll)

        linha = BoxLayout(size_hint_y=None, height=120, spacing=8)
        self.entrada = TextInput(multiline=False)
        self.entrada.bind(on_text_validate=self.enviar)
        botao = Button(text="Enviar", size_hint_x=0.3)
        botao.bind(on_release=self.enviar)
        linha.add_widget(self.entrada)
        linha.add_widget(botao)
        raiz.add_widget(linha)

        self.escrever("A.N.N.E. 0.1 ALPHA")
        self.escrever(self.anne.personalidade.apresentar())
        return raiz

    def escrever(self, texto):
        self.chat.text += texto + "\n\n"
        Clock.schedule_once(
            lambda dt: setattr(self.scroll, "scroll_y", 0)
        )
