from kivymd.uix.navigationdrawer import MDNavigationDrawer,MDNavigationDrawerMenu,MDNavigationDrawerItem,MDNavigationDrawerItemText,MDNavigationDrawerLabel
from kivy.metrics import dp

from ui import IconButton,OptionsTabs,DropMenu


class TabBar(MDNavigationDrawer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = 'tab'
        self.drawer_type = 'modal'
        self.anchor = 'right'
        self.radius = (dp(10), 0, 0, dp(10))
        self.width = dp(200)
        
        menu = MDNavigationDrawerMenu()
        menu.spacing = 10
        
        label = MDNavigationDrawerLabel(text="Tabs")
        #divider = MDNavigationDrawerDivider()
        menu.add_widget(label)
        #menu.add_widget(divider)
       
        for x in range(5):
            items = MDNavigationDrawerItem()
            items.btn = IconButton("svg/add.png","svg/add.png")
            items.add_widget(items.btn)
            items.add_widget(MDNavigationDrawerItemText(text="Tabs",font_size=24))
            items.opt = OptionsTabs(items.btn)
            items.height = dp(36)
            items.md_bg_color = (1,1,1,1)
            menu.add_widget(items)

        
        

        self.add_widget(menu)







#class NewTabView()