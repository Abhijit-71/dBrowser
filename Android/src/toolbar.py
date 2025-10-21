#for toolbar and all buttons
from kivy.uix.textinput import TextInput
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.label import MDLabel
from ui import IconButton
from kivymd.uix.textfield import MDTextField,MDTextFieldHelperText,textfield
from kivy.uix.image import Image
from kivy.graphics import Color , RoundedRectangle,Line
from kivymd.uix.button import MDIconButton
from tabmanager import DropMenu
from kivy.metrics import dp


class CustomBar(MDBoxLayout):
    def __init__(self,size, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint = size
        self.height = dp(56)
        self.padding = [10, 10, 10, 10]
        self.spacing = 10
        self.md_bg_color = (33/225, 35/225, 56/225, 1)
        # Left icon
       
        self.add_widget(IconButton(
            'svg/google_logo.png',
            'svg/google_logo.png',
            on_release = lambda x:MDApp.get_running_app().open_tab_drawer()  #type:ignore
        ))
        # Title or search field
        self.add_widget(UrlBar())

        """self.add_widget(MDIconButton(
            icon="numeric-7-box-multiple", #plus-box-multiple
            theme_icon_color="Custom",
            icon_color=(1, 1, 1, 1),
            size_hint=(None, None),
            font_size=dp(14),
            on_release = lambda x:MDApp.get_running_app().open_tab_drawer()  #type:ignore
        ))"""
        self.add_widget(IconButton(
            'svg/google_logo.png',
            'svg/google_logo.png',
            on_release = lambda x:MDApp.get_running_app().open_tab_drawer()  #type:ignore
        ))

        # Right icon
        self.btn =IconButton(
            'svg/google_logo.png',
            'svg/google_logo.png',
        )
        
        self.add_widget(self.btn)
        self.dropdown = DropMenu(self.btn)



class UrlBar(MDTextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = 'outlined'
        self.size_hint = (0.5, None)
        self.height = dp(32)
        self.pos_hint = {"center_y": 0.5}
        self.radius = [8, 8, 8, 8]
        self.hint_text = "hi"
        self.hint_text_color = (1, 1, 1, 0.7)  # White hint text
        self.fill_color = (1, 1, 1, 1)  # Light background
        self.text_color = (1, 1, 1, 0.6)  
        
class url(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text = "Search here..."
        self.multiline = False
        self.padding = [10,10,10,10]
        self.pos_hint = {"center_y": 0.5}
        self.hint_text_color = (1,1,1,1)
        #self.background_color = (67/225,72/225,109/225)
        self.background_color = (0,0,0,0)
        self.font_size = 16
        self.size_hint = (0.5, 0.8)

        with self.canvas.before: #type:ignore
            Color(1, 1, 1, 0.8)
            self.border_line = Line(rounded_rectangle=(self.x, self.y, self.width, self.height, dp(6)), width=1)
        
        self.bind(pos=self.update_line, size=self.update_line) #type:ignore

    def update_line(self, *args):
        self.border_line.rounded_rectangle = (self.x, self.y, self.width, self.height, 10)
