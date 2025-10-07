"""from PyQt6.QtWidgets import (
    QSizePolicy, QWidget, QLabel, QHBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView


class Navigation(QWidget):
    def __init__(self,browser:QWebEngineView,color="#e23c3cdc"):
        super().__init__()
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(5)

        self.back = IconButton('svg/back.svg',25)
        #self.back.setStyleSheet("background: transparent; border: none;")
        self.back.clicked.connect(browser.back)
        layout.addWidget(self.back)

        self.forward = IconButton('svg/forward.svg',25)
        #self.forward.setStyleSheet("background: transparent; border: none;")
        self.forward.clicked.connect(browser.forward)
        layout.addWidget(self.forward)

        self.reload = IconButton('svg/reload.svg',25)
        #self.reload.setStyleSheet("background: transparent; border: none;")
        self.reload.clicked.connect(browser.reload)
        layout.addWidget(self.reload)
        
        layout.addStretch()
        self.setLayout(layout)
        self.setFixedHeight(40) 
        

class Toolbar(QWidget):
    def __init__(self,navbar,color="#ffffff00"):
        super().__init__()
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(5)
        layout.addWidget(navbar)
        layout.addStretch()

        self.title = QLabel("dBrowser")
        
        self.title.setStyleSheet("color: white; font-weight: bold; font-size: 16px;")
        
        layout.addWidget(self.title)
        self.setLayout(layout)
        self.setStyleSheet(f"background-color: {color};")
        self.setFixedHeight(40)"""



from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt
from .coreui import HoverButton , IconButton

class Navigation(QWidget):
    def __init__(self, browser:QWebEngineView, color="#34495e"):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 8, 15, 8)
        layout.setSpacing(8)

        self.back = IconButton('svg/back.svg', 25)
        self.back.clicked.connect(browser.back)
        layout.addWidget(self.back)

        self.forward = IconButton('svg/forward.svg', 25)
        self.forward.clicked.connect(browser.forward)
        layout.addWidget(self.forward)

        self.reload = IconButton('svg/reload.svg', 25)
        self.reload.clicked.connect(browser.reload)
        layout.addWidget(self.reload)
        
        layout.addStretch()
        
        self.setStyleSheet(f"""
            Navigation {{
                background-color: {color};
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }}
            QPushButton {{
                background: transparent;
                border: none;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                background-color: rgba(255, 255, 255, 0.1);
            }}
            QPushButton:pressed {{
                background-color: rgba(255, 255, 255, 0.2);
            }}
        """)
        self.setFixedHeight(45)

class Toolbar(QWidget):
    def __init__(self, navbar, color="#2c3e50"):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(navbar)
        layout.addStretch()

        self.title = QLabel("dBrowser")
        self.title.setStyleSheet("color: white; font-weight: bold; font-size: 16px; padding-right: 15px;")
        layout.addWidget(self.title)
        
        self.setStyleSheet(f"""
            Toolbar {{
                background-color: {color};
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }}
        """)
        self.setFixedHeight(45)
        
