from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp

from main import DialogManager


class HotReload(MDApp):
    KV_FILES = ['main.kv']
    DEBUG = True

    def build_app(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "700"  # Define a intencidade da cor
        self.theme_cls.accent_palette = "Cyan"
        self.theme_cls.accent_hue = "400" 
        self.dialog_manager = DialogManager(self)
        LabelBase.register(name="MPoppins", fn_regular="assets/fonts/Poppins-Medium.ttf")
        LabelBase.register(name="RPoppins", fn_regular="assets/fonts/Poppins-Regular.ttf")

        return Builder.load_file('main.kv')

if __name__ == '__main__':
    HotReload().run()
