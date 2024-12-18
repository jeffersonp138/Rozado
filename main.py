from datetime import datetime

from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen

Window.size = (310, 580)


class Home(MDScreen):
    ...


class LayoutDespesaDialog(MDBoxLayout):
    date_label_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.date_label_text = datetime.now().strftime('%d/%m/%Y %H:%M')

    def show_date_picker(self):

        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        # Atualiza o texto do date_label com a data selecionada
        self.date_label_text = value.strftime('%d/%m/%Y')

    def reset_fields(self):
        # self.date_label_text = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.ids.value_input.text = ""



class DialogManager:
    def __init__(self, app):
        self.app = app
        self.dialog = None

    def show_dialog_despesa(self):
        if not self.dialog:
            self.dialog = self.create_dialog_despesa()

        self.dialog.open()

    def create_dialog_despesa(self):
        content = LayoutDespesaDialog()

        dialog = MDDialog(
            type='custom',
            content_cls=content,
            size_hint=(0.9, None),
            height=self.calculate_dialog_height(content),
            buttons=[
                MDRaisedButton(
                    text="Cancelar",
                    on_release=lambda x: dialog.dismiss()
                ),
                MDRaisedButton(
                    text="Salvar",
                    on_release=lambda *args: self.save_despesa()
                ),
            ],
        )
        return dialog

    def calculate_dialog_height(self, content):
        # Calcula a altura necessária para o diálogo com base no conteúdo
        return content.minimum_height

    def save_despesa(self):
        content = self.dialog.content_cls
        valor_selecionado = content.ids.value_input.text
        data_selecionada = content.date_label_text
        print(
            f"Valor: {valor_selecionado}, Data: {data_selecionada}")

        content.reset_fields()

        self.dialog.dismiss()


class Rozado(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "700"  # Define a intencidade da cor
        self.theme_cls.accent_palette = "Cyan"
        self.theme_cls.accent_hue = "400"

        LabelBase.register(
            name="MPoppins", 
            fn_regular="assets/fonts/Poppins-Medium.ttf"
            )
        LabelBase.register(
            name="RPoppins", 
            fn_regular="assets/fonts/Poppins-Regular.ttf"
            )

        self.dialog_manager = DialogManager(self)

        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('main.kv'))
        return screen_manager


if __name__ == '__main__':

    Rozado().run()
