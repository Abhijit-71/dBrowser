#entry point of app main window

import platform 
import os

from kivy.app import App
from kivy.core.window import Window
from ui import MainWindow
from toolbar import ToolBar


IS_ANDROID = platform.system() == "Linux" and "ANDROID_ROOT" in os.environ  #checks if android , for development only (ui)
print(IS_ANDROID)

if IS_ANDROID:
    from browser import Browser
    browser = Browser().webview
else:
    from browser import demoBrowser
    browser = demoBrowser().webview

Window.clearcolor = (14/255, 15/255, 25/255 ,1)
Window.size = (320,640)
Window.resizable = True

class Main(App):
    def build(self):
        toolbar = ToolBar(size=((1,0.05)))
        return MainWindow(toolbar,browser)
        


if __name__ == '__main__':
    Main().run()