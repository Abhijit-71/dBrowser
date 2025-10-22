#for core ui components 

from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu



class IconButton(RectangularRippleBehavior,Button):
    def __init__(self,normal:str,down:str,**kwargs):
        super().__init__(**kwargs)
        self.background_normal = normal
        self.background_down = down
        self.border = (0, 0, 0, 0)
        self.size_hint = (None, None) 
        self.size = (42,42)
        self.pos_hint = {"center_y": 0.5}



     
class DropMenu(MDDropdownMenu):
    def __init__(self,caller_btn, **kwargs):
        menu_items = [
            {
                "text": "BookMark",
                "icon": "star",
                "on_release": lambda x="BookMark": self.menu_callback(x)
            },
            {
                "text": "History",
                "icon": "clock",
                "on_release": lambda x="History": self.menu_callback(x)
            },
            {
                "text": "Help",
                "icon": "help-circle",
                "on_release": lambda x="Help": self.menu_callback(x)
            },
            {
                "text": "Customize",
                "icon": "brush",
                "on_release": lambda x="Customize": self.menu_callback(x)
            },
            {
                "text": "Settings",
                "icon": "cog",
                "font_size":16,
                "on_release": lambda x="Settings": self.menu_callback(x)
            },
        ]
        super().__init__(**kwargs)
        self.width = dp(150)
        #self.height = dp(200)
        self.caller = caller_btn
        self.items = menu_items
        self.elevation =15
        self.allow_hover = "True"
        self.padding = (10,0,10,0)
        self.position = 'bottom'
        self.ver_growth="down"
        
        #self.background_color = (1,1,1,1)

        self.caller.bind(on_release=lambda x: self.open())


    def menu_callback(self, text_item):
        print(f"Selected: {text_item}")
        self.dismiss()    




class OptionsTabs(MDDropdownMenu):
    def __init__(self,caller_btn, **kwargs):
        menu_items = [
            {
                "text": "Delete",
                "icon": "brush",
                "on_release": lambda x="Deleted Tab": self.menu_callback(x)
            }
        ]
        super().__init__(**kwargs)
        self.width = dp(150)
        #self.height = dp(200)
        self.background_color = (0.7,0.5,0.5,1)
        self.caller = caller_btn
        self.items = menu_items
        self.elevation =15
        self.allow_hover = "True"
        self.padding = (10,0,10,0)
        self.position = 'bottom'
        self.ver_growth="down"

        self.caller.bind(on_release=lambda x: self.open())


    def menu_callback(self, text_item):
        print(f"Selected: {text_item}")
        self.dismiss()



     
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
        


