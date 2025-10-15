from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics import Color , RoundedRectangle


class ToolBar(BoxLayout):
    def __init__(self,size:tuple):
        super().__init__()
        self.orientation = "horizontal"
        self.size_hint = size
        self.spacing = 5
        self.padding = 2
        self.add_widget(Image(source='svg/google_logo.png', allow_stretch=True, keep_ratio=True ,size_hint=(0.05, 0.9)))
        self.add_widget(URLBar())
        self.add_widget(img_btn("svg/google_logo.png","svg/google_logo.png"))
        self.add_widget(img_btn("svg/google_logo.png","svg/google_logo.png"))

        with self.canvas.before:  # type:ignore
            Color(0.2, 0.4, 0.6, 0.2)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[5] 
            )

        self.bind(pos=self.update_rect, size=self.update_rect) # type:ignore
    
    def update_rect(self,*args):
        self.rect.pos = self.pos
        self.rect.size = self.size



class URLBar(TextInput):
    def __init__(self):
        super().__init__()
        self.hint_text = "Search here..."
        self.multiline = False
        self.size_hint = (0.5, 0.9)
        self.background_color = (0, 0, 0, 0)

        with self.canvas.before:  # type:ignore
            Color(0.2, 0.4, 0.6, 0.2)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[5] 
            )

        self.bind(pos=self.update_rect, size=self.update_rect) # type:ignore
    
    def update_rect(self,*args):
        self.rect.pos = self.pos
        self.rect.size = self.size


    
class img_btn(Button):
    def __init__(self,normal:str,down:str):
        super().__init__()
        self.background_normal = normal
        self.background_down = down
        self.border = (0, 0, 0, 0)
        self.size_hint = (None, 1) 
        self.width = 40
        
