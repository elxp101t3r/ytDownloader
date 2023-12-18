from pytube import YouTube
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window


Window.size=(500,600)

class App(MDApp):
    def build(self):
        layout = MDRelativeLayout(md_bg_color = [248/255, 200/255, 220/255])
        
        
        return layout

if __name__ == '__main__':
    App().run()