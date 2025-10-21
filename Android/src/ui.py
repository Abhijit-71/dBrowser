#for core ui components 

from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior, CircularRippleBehavior
from kivy.metrics import dp



class IconButton(Button):
    def __init__(self,normal:str,down:str,**kwargs):
        super().__init__(**kwargs)
        self.background_normal = normal
        self.background_down = down
        self.border = (0, 0, 0, 0)
        self.size_hint = (None, 1) 
        self.size = (dp(36), dp(36))
        self.pos_hint = {"center_y": 0.5}


     
class MainScreen(BoxLayout):
    def __init__(self,toolbar,window):
        super().__init__()
        self.orientation = 'vertical'
        self.spacing = 10
        #self.padding = 5
        self.add_widget(toolbar)
        self.add_widget(window.webview)


class MainWindow(MDNavigationLayout):
    def __init__(self,tabbar,screen,*args, **kwargs):
        super().__init__(*args, **kwargs)
        sc = Screen()
        sc.add_widget(screen)
        sm = ScreenManager()
        sm.add_widget(sc)
        self.add_widget(sm)
        self.add_widget(tabbar)
        


