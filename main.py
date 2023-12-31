from functools import partial
from pytube import YouTube
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.video import Video
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
import re
from kivymd.uix.textfield import MDTextField
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.window import Window


Window.size=(500,600)

class App(MDApp):
    def getLinkInfo(self, event, layout):
        self.link = self.link_input.text
        self.checklink = re.match("^https://www.youtube.com/.*", self.link)
        
        if self.checklink:
            self.errorLabel.text = ''
            self.errorLabel.pos_hint = {'center_x':0.5, 'center_y':20}
            try:
                self.errorLabel.text = ''
                self.errorLabel.pos_hint = {'center_x':0.5, 'center_y':20}
                
                self.yt = YouTube(self.link)
                self.title = str(self.yt.title)
                self.views = str(self.yt.views)
                self.length = str(self.yt.length)
                
                
                self.titleLabel.text = "Title: "+ self.title + " "
                self.titleLabel.pos_hint={'center_x': 0.5, 'center_y': 0.4}
                
                
                self.viewsLabel.text = "Views: " + self.views + " "
                self.viewsLabel.pos_hint={'center_x': 0.5, 'center_y': 0.35}
                
                
                self.lengthLabel.text = "Length: " + self.length + " "
                self.lengthLabel.pos_hint={'center_x': 0.5, 'center_y': 0.30}
                
                self.downloadButton.text = 'Download'
                self.downloadButton.pos_hint = {'center_x': 0.5, 'center_y': 0.15}
                self.downloadButton.size_hint = (.3, .1)
                
                
                self.video = self.yt.streams.filter(file_extension='mp4').order_by('resolution').desc()
                
                
                self.dropDown = DropDown()
                
                
                for video in self.video:
                    btn = Button(text=video.resolution, size_hint_y=None, height=30)
                    btn.bind(on_release=lambda btn:self.dropDown.select(btn.text))
                    
                    self.dropDown.add_widget(btn)
                    
                self.main_button = Button(text='144p', size_hint=(None, None), pos=(350, 65), height=50)
                self.main_button.bind(on_release=self.dropDown.open)
                self.dropDown.bind(on_select=lambda instance, x:setattr(self.main_button, 'text', x))
                
                layout.add_widget(self.main_button)
                
            except:
                self.errorLabel.text = 'Network or unknown error'
                self.errorLabel.pos_hint = {'center_x':0.5, 'center_y':0.4}
            
        else:
            self.errorLabel.text = 'Invalid Link!'
            self.errorLabel.pos_hint = {'center_x':0.5, 'center_y':0.4}
           
            
        
    def download(self, event, layout):
        self.ys = self.yt.streams.filter(file_extension='mp4').filter(res=self.main_button.text).first()
        print('Downloading...')
        self.ys.download()
        print('Completed!')
                
               
    def build(self):
        layout = MDRelativeLayout()
        video = Video(source='bg.mp4', state='play', options={'eos': 'loop'})
        self.img = Image(source='logo.png', size_hint= (.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.90})
        
        self.youtubeLink = Label(text='URL', pos_hint={'center_x': 0.5 , 'center_y': .75}, size_hint=(1,1), font_size=20, color=(0,0,0))
        
        self.link_input = MDTextField(text='', pos_hint={'center_x': 0.5,'center_y': 0.65}, text_color_focus=[0,0,0,1], line_color_normal=[0,0,0,1],line_color_focus=[0,0,0,1], size_hint_x=None, width=300)
        
        self.link_button = MDRectangleFlatButton(text='search', pos_hint={'center_x':0.5, "center_y": 0.5}, size_hint=(.2, .1),font_size=15, line_color=[0,0,0,1], text_color=[1,1,1,1], md_bg_color=[0,0,0, 1])
        
        
        self.link_button.bind(on_press= partial(self.getLinkInfo, layout))
        
        self.titleLabel = Label(text='', pos_hint={'center_x': 0.5 , 'center_y': 20}, size_hint=(1,1), font_size=20)
        
        self.viewsLabel = Label(text='', pos_hint={'center_x': 0.5 , 'center_y': 20}, size_hint=(1,1), font_size=20)
        
        self.lengthLabel = Label(text='', pos_hint={'center_x': 0.5 , 'center_y': 20}, size_hint=(1,1), font_size=20)
        
        self.downloadButton = Button(pos_hint= {'center_x': 0.5,'center_y': 20}, size_hint=(.2, .1), size=(75, 75), bold=True, font_size=24, background_color=(0,0,0))
        
        self.downloadButton.bind(on_press=partial(self.download, layout))
        self.errorLabel = Label(text='', pos_hint={'center_x':0.5, 'center_y':20}, size_hint=(1,1), font_size=20, color=(1,0,0))
        
        layout.add_widget(video)
        layout.add_widget(self.img)
        layout.add_widget(self.youtubeLink)
        layout.add_widget(self.link_input)
        layout.add_widget(self.link_button)
        layout.add_widget(self.titleLabel)
        layout.add_widget(self.viewsLabel)
        layout.add_widget(self.lengthLabel)
        layout.add_widget(self.downloadButton)
        layout.add_widget(self.errorLabel)
        
        return layout


if __name__ == '__main__':
    
    App().run()