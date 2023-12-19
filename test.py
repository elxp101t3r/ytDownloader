from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField

class App(MDApp):
    def build(self):
        screen = Screen()
        search = MDTextField(text='', pos_hint={'center_x': 0.5,'center_y': 0.65}, size_hint_x=None, width=300)
        screen.add_widget(search)
        return screen

App().run()