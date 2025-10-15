# using generally for unit test within this venv

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle, Line, Ellipse, Rectangle
from kivy.graphics.texture import Texture
from kivy.core.window import Window

Window.size = (400, 700)
Window.clearcolor = (0.95, 0.95, 0.95, 1)


# 1. ROUNDED BUTTON
class RoundedButton(Button):
    def __init__(self, bg_color=(0.2, 0.4, 0.8, 1), radius=15, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.bg_color = bg_color
        self.radius = radius
        
        with self.canvas.before: #type:ignore
            self.bg = Color(*bg_color)  # Changed from self.color to self.bg
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[radius])
        
        self.bind(pos=self.update_rect, size=self.update_rect)#type:ignore
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# 2. CARD WIDGET (like Material Design cards)
class Card(BoxLayout):
    def __init__(self, bg_color=(1, 1, 1, 1), radius=10, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 15
        self.spacing = 10
        
        with self.canvas.before: #type:ignore
            # Shadow effect (darker background behind)
            Color(0, 0, 0, 0.1)
            self.shadow = RoundedRectangle(
                pos=(self.x + 2, self.y - 2),
                size=self.size,
                radius=[radius]
            )
            # Main card
            Color(*bg_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[radius])
        
        self.bind(pos=self.update_graphics, size=self.update_graphics)#type:ignore
    
    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.shadow.pos = (self.x + 2, self.y - 2)
        self.shadow.size = self.size


# 3. BORDERED BUTTON
class BorderedButton(Button):
    def __init__(self, bg_color=(1, 1, 1, 1), border_color=(0.2, 0.4, 0.8, 1), 
                 border_width=2, radius=8, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.radius = radius
        self.border_width = border_width
        self.border_color = border_color
        
        with self.canvas.before:#type:ignore
            Color(*bg_color)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[radius])
            
        with self.canvas.after:#type:ignore
            Color(*border_color)
            self.border_line = Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, radius),
                width=border_width
            )
        
        self.bind(pos=self.update_graphics, size=self.update_graphics)#type:ignore
    
    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.border_line.rounded_rectangle = (self.x, self.y, self.width, self.height, self.radius)


# 4. CIRCLE BUTTON (for icons)
class CircleButton(Button):
    def __init__(self, bg_color=(0.2, 0.4, 0.8, 1), **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        self.size_hint = (None, None)
        self.size = (60, 60)
        
        with self.canvas.before:#type:ignore
            Color(*bg_color)
            self.circle = Ellipse(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_circle, size=self.update_circle)#type:ignore
    
    def update_circle(self, *args):
        self.circle.pos = self.pos
        self.circle.size = self.size


# 5. GRADIENT BUTTON (using texture)
class GradientButton(Button):
    def __init__(self, color1=(0.2, 0.4, 0.8), color2=(0.4, 0.6, 1.0), **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)
        
        # Create gradient texture
        texture = Texture.create(size=(1, 256), colorfmt='rgb')
        buf = []
        for i in range(256):
            t = i / 255.0
            r = int((color1[0] * (1 - t) + color2[0] * t) * 255)
            g = int((color1[1] * (1 - t) + color2[1] * t) * 255)
            b = int((color1[2] * (1 - t) + color2[2] * t) * 255)
            buf.extend([r, g, b])
        
        buf = bytes(buf)
        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        
        with self.canvas.before:#type:ignore
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size, texture=texture)
        
        self.bind(pos=self.update_rect, size=self.update_rect)#type:ignore
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# 6. TOOLBAR (custom styled)
class StyledToolbar(BoxLayout):
    def __init__(self, bg_color=(0.15, 0.15, 0.15, 1), **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 60
        self.padding = 10
        self.spacing = 10
        
        with self.canvas.before:#type:ignore
            Color(*bg_color)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_rect, size=self.update_rect)#type:ignore
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


# DEMO APP
class StylingDemo(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Toolbar
        toolbar = StyledToolbar()
        toolbar.add_widget(Label(text='Styling Examples', color=(1, 1, 1, 1), bold=True))
        root.add_widget(toolbar)
        
        # Scrollable content
        content = BoxLayout(orientation='vertical', spacing=15, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))#type:ignore
        
        # Rounded button
        btn1 = RoundedButton(text='Rounded Button', size_hint=(1, None), height=50)
        content.add_widget(btn1)
        
        # Bordered button
        btn2 = BorderedButton(
            text='Bordered Button',
            size_hint=(1, None),
            height=50,
            color=(0.2, 0.4, 0.8, 1)
        )
        content.add_widget(btn2)
        
        # Gradient button
        btn3 = GradientButton(text='Gradient Button', size_hint=(1, None), height=50)
        content.add_widget(btn3)
        
        # Circle buttons row
        circle_row = BoxLayout(size_hint=(1, None), height=70, spacing=10)
        for i in range(4):
            cb = CircleButton(text=str(i+1))
            circle_row.add_widget(cb)
        content.add_widget(circle_row)
        
        # Card example
        card = Card(size_hint=(1, None), height=150)
        card.add_widget(Label(text='Card Title', bold=True, size_hint_y=0.3))
        card.add_widget(Label(text='This is a card with shadow effect\nand rounded corners'))
        content.add_widget(card)
        
        # Another card
        card2 = Card(size_hint=(1, None), height=120, bg_color=(0.9, 0.95, 1, 1))
        card2.add_widget(Label(text='Colored Card', color=(0.2, 0.2, 0.2, 1)))
        card2.add_widget(RoundedButton(
            text='Action Button',
            size_hint=(1, None),
            height=40,
            bg_color=(0.2, 0.6, 0.4, 1),
            radius=20
        ))
        content.add_widget(card2)
        
        root.add_widget(content)
        return root


if __name__ == '__main__':
    StylingDemo().run()