#for core ui components 


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button






     
class MainWindow(BoxLayout):
    def __init__(self,toolbar,browser):
        super().__init__()
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 5
        self.add_widget(toolbar)
        self.add_widget(browser)