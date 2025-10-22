#for toolbar and all buttons
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from ui import IconButton
from kivy.graphics import Color ,Line
from tabmanager import DropMenu
from kivy.metrics import dp


class CustomBar(MDBoxLayout):
    def __init__(self,size, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint = size
        self.height = dp(64)
        self.padding = [10, 10, 10, 10]
        self.spacing = 5
        self.md_bg_color = (14/255, 15/255, 25/255 ,1)
        
       
        self.add_widget(IconButton(
            'svg/home.png',
            'svg/home_pressed.png',
            on_release = lambda x:MDApp.get_running_app().open_tab_drawer()  #type:ignore
        ))
        
        self.add_widget(UrlBar())

        self.add_widget(IconButton(
            'svg/add.png',
            'svg/add_pressed.png',
            on_release = lambda x:MDApp.get_running_app().open_tab_drawer()  #type:ignore
        ))

        self.menu =IconButton(
            'svg/dots.png',
            'svg/dots_pressed.png',
        )
        
        self.add_widget(self.menu)
        self.dropdown = DropMenu(self.menu)



class UrlBar(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = [15,0,30,0]
        self.pos_hint = {"center_y": 0.5}
        self.add_widget(url())
        self.size_hint = (0.6, 0.8)
        
class url(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = "Search here..."
        self.multiline = False
        self.padding = [10,10,10,10]
        self.pos_hint = {"center_y": 0.5}
        self.hint_text_color = (1,1,1,1)
        self.foreground_color = (1,1,1,1)
        self.background_active = "False"
        self.background_normal = "False"
        self.background_color = (33/255, 35/255, 56/255, 1)
        self.font_size = 16
        
        
