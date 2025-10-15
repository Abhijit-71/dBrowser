
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button





     
class MainWindow(BoxLayout):
    def __init__(self,toolbar):
        super().__init__()
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 5
        self.add_widget(toolbar)
        self.add_widget(Button(text="hi",size_hint=(1,0.9),background_color=(0, 0.5, 1, 1),  # blue
            color=(1, 1, 1, 1)))