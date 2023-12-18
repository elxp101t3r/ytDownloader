from pytube import YouTube
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button

class App(MDApp):
    def build(self):
        layout = MDRelativeLayout()
        return layout

if __name__ == '__main__':
    App().run()