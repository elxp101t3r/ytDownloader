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
        layout = MDRelativeLayout(md_bg_color = [124/255, 200/255, 255/255])
        self.img = Image(source='logo.png', size_hint= (.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.90})
        self.youtubeLink = Label(text='URL', pos_hint={'center_x': 0.5 , 'center_y': .75}, size_hint=(1,1), font_size=20, color=(0,0,0))
        
        layout.add_widget(self.img)
        layout.add_widget(self.youtubeLink)
       
        return layout

if __name__ == '__main__':
    App().run()