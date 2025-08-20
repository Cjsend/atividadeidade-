import requests  # Para consumir a API
from kivy.uix.boxlayout import BoxLayout # Layout para organizar os widgets
from kivy.uix.button import Button # Botão para interação
from kivy.uix.label import Label # Rótulo para exibir a piada
from kivy.uix.textinput import TextInput # Campo de entrada de texto
from kivy.app import App # Classe principal do aplicativo

class WelcomeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.title_label = Label(
            text='App de boas vindas',
            font_size=24,
            bold=True,
            size_hint=(1, 0.3),
            halign='center',
            valign='middle'
        )

        self.title_label.bind(size=self.title_label.setter('text_size'))
        self.layout.add_widget(self.title_label)

        self.input = TextInput(hint_text='Digite seu nome', size_hint_y=None, height=40)
        self.layout.add_widget(self.input)

        self.input = TextInput(hint_text='Digite sua idade', size_hint_y=None, height=40)
        self.layout.add_widget(self.input)

        self.button = Button(text='Enviar', size_hint_y=None, height=40, background_color=(1, 0, 0, 1))
        self.button.bind(on_press=self.on_button_press)
        self.layout.add_widget(self.button)

        self.label = Label(text='', size_hint_y=None, height=40)
        self.layout.add_widget(self.label)

        return self.layout

    def on_button_press(self, instance):
        idade = self.input.text.strip()
        if idade:
            self.label.text = f'Bem-vindo(a), {idade}!'
        else:
            self.label.text = 'Por favor, digite seu nome.'

    def on_button_press(self, instance):
        nome = self.input.text.strip()
        if nome:
            self.label.text = f'Bem-vindo(a), {nome}!'
        else:
            self.label.text = 'Por favor, digite seu nome.'

if __name__ == '__main__':
    WelcomeApp().run()