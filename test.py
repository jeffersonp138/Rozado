from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

KV = '''
MDBoxLayout:
    orientation: 'vertical'
    padding: "12dp"
    spacing: "10dp"
    

    MDTextField:
        id: input_field
        hint_text: "Enter something"
        mode: "rectangle"
'''

class CustomDialogApp(MDApp):
    dialog = None

    def build(self):
        return MDFlatButton(
            text="Show Custom Dialog",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            on_release=self.show_dialog,
        )

    def show_dialog(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Custom Dialog",
                type="custom",
                content_cls=Builder.load_string(KV),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=self.close_dialog
                    ),
                    MDFlatButton(
                        text="SUBMIT",
                        on_release=self.submit_action
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def submit_action(self, *args):
        input_text = self.dialog.content_cls.ids.input_field.text
        print(f"Submitted text: {input_text}")
        self.close_dialog()

CustomDialogApp().run()
