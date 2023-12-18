from functools import partial
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
    def getLinkInfo(self, event, window):
        self.link = self.link_input.text
        self.yt = YouTube(self.link)
        print(self.yt.title)
        print(self.yt.views)
        print(self.yt.length)
        
        
    def build(self):
        layout = MDRelativeLayout(md_bg_color = [124/255, 200/255, 255/255])
        
        self.img = Image(source='logo.png', size_hint= (.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.90})
        
        self.youtubeLink = Label(text='URL', pos_hint={'center_x': 0.5 , 'center_y': .75}, size_hint=(1,1), font_size=20, color=(0,0,0))
        
        self.link_input = TextInput(text='', pos_hint={'center_x': 0.5 , 'center_y': 0.65 }, size_hint= (1, None), height=48, font_size=29, foreground_color=(0, 0, 0))
        
        self.link_button = Button(text='Download', pos_hint={'center_x': 0.5 , 'center_y': 0.5 }, size_hint= (.2, .1), font_size=20, background_color=[0,0,0])
        
        
        self.link_button.bind(on_press= partial(self.getLinkInfo, layout))
        
        
        layout.add_widget(self.img)
        layout.add_widget(self.youtubeLink)
        layout.add_widget(self.link_input)
        layout.add_widget(self.link_button)

        return layout


if __name__ == '__main__':
    App().run()