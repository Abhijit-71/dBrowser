from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationDrawerMenu,MDNavigationDrawerLabel
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu


class TabBar(MDNavigationDrawer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = 'tab'
        self.drawer_type = 'modal'
        self.anchor = 'right'
        self.radius = (dp(10), 0, 0, dp(10))
        self.width = dp(200)
        
        menu = MDNavigationDrawerMenu()
        menu.add_widget(MDNavigationDrawerLabel(text="Tab Manager"))
        
        self.add_widget(menu)

class DropMenu(MDDropdownMenu):
    def __init__(self,caller_btn, **kwargs):
        menu_items = [
            {
                "text": "Settings",
                "icon": "cog",
                "on_release": lambda x="Settings": self.menu_callback(x)
            },
            {
                "text": "Help",
                "icon": "help-circle",
                "on_release": lambda x="Help": self.menu_callback(x)
            },
            {
                "text": "Logout",
                "icon": "logout",
                "on_release": lambda x="Logout": self.menu_callback(x)
            },
        ]
        super().__init__(**kwargs)
        self.width = dp(150)
        self.caller = caller_btn
        self.items = menu_items
        self.position = 'bottom'
        self.ver_growth="down"
        
        self.background_color = (1,1,1,1)

        self.caller.bind(on_release=lambda x: self.open())


    def menu_callback(self, text_item):
        print(f"Selected: {text_item}")
        self.dismiss()