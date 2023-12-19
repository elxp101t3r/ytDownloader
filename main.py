from functools import partial
from pytube import YouTube
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window


Window.size=(500,600)

class App(MDApp):
    def getLinkInfo(self, event, layout):
        self.link = self.link_input.text
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
            btn = Button(text=video.resolution, size_hint=None, height=30)
            btn.bind(on_release=lambda btn:self.dropDown.select(btn.text))
            
            self.dropDown.add_widget(btn)
            
        self.main_button = Button(text='144p', size_hint=(None, None), pos=(350, 65), height=50)
        self.main_button.bind(on_release=self.dropDown.open)
        self.dropDown.bind(on_select=lambda instance, x:setattr(self.main_button, 'text', x))
        
        layout.add_widget(self.main_button)
            
            
            
        
    def download(self, event, layout):
        self.ys = self.yt.streams.get_highest_resolution()
        print('Downloading...')
        self.ys.download()
        print('Completed!')
                
               
    def build(self):
        layout = MDRelativeLayout(md_bg_color = [124/255, 200/255, 255/255])
        
        self.img = Image(source='logo.png', size_hint= (.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.90})
        
        self.youtubeLink = Label(text='URL', pos_hint={'center_x': 0.5 , 'center_y': .75}, size_hint=(1,1), font_size=20, color=(0,0,0))
        
        self.link_input = TextInput(text='', pos_hint={'center_x': 0.5 , 'center_y': 0.65 }, size_hint= (1, None), height=48, font_size=29, foreground_color=(0, 0, 0))
        
        self.link_button = Button(text='Search', pos_hint={'center_x': 0.5 , 'center_y': 0.5 }, size_hint= (.2, .1), font_size=20, background_color=[0,0,0])
        
        
        self.link_button.bind(on_press= partial(self.getLinkInfo, layout))
        
        self.titleLabel = Label(text='', pos_hint={'center_x': 0.5 , 'center_y': 20}, size_hint=(1,1), font_size=20)
        
        self.viewsLabel = Label(text='', pos_hint={'center_x': 0.5 , 'center_y': 20}, size_hint=(1,1), font_size=20)
        
        self.lengthLabel = Label(text='', pos_hint={'center_x': 0.5 , 'center_y': 20}, size_hint=(1,1), font_size=20)
        
        self.downloadButton = Button(pos_hint= {'center_x': 0.5,'center_y': 20}, size_hint=(.2, .1), size=(75, 75), bold=True, font_size=24, background_color=(0,0,0))
        
        self.downloadButton.bind(on_press=partial(self.download, layout))
        
        
        layout.add_widget(self.img)
        layout.add_widget(self.youtubeLink)
        layout.add_widget(self.link_input)
        layout.add_widget(self.link_button)
        layout.add_widget(self.titleLabel)
        layout.add_widget(self.viewsLabel)
        layout.add_widget(self.lengthLabel)
        layout.add_widget(self.downloadButton)

        return layout


if __name__ == '__main__':
    
    App().run()