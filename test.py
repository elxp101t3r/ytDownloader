from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class App(MDApp):
    def build(self):
        screen = Screen()
        btn = MDRectangleFlatButton(text='search', pos_hint={'center_x':0.5, "center_y": 0.5}, size_hint=(.2, .1), font_size=20, md_color=[0,0,0,1])
        screen.add_widget(btn)
        return screen
    
App().run()