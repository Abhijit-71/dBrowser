#entry point of app main window

from kivymd.app import MDApp
from kivy.core.window import Window
from ui import MainWindow , MainScreen
from toolbar import CustomBar
from browser import demoBrowser
from tabmanager import TabBar



Window.clearcolor = (0.7, 0.7, 0.7 ,0.7)
Window.size = (320,640)
Window.resizable = True
window = demoBrowser()

class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Purple"  
        topbar = CustomBar(size=(1,0.1))
        self.tabbar = TabBar()
        screen = MainScreen(topbar,window)
        return MainWindow(self.tabbar,screen)
    
    def open_tab_drawer(self):
        self.tabbar.set_state("toggle") #type:ignore
        


if __name__ == '__main__':
    Main().run()