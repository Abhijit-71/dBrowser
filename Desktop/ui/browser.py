from PyQt6.QtWidgets import QWidget , QVBoxLayout
from .toolbar import Toolbar , Navigation , URLTab
from PyQt6.QtCore import Qt , QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView


class BrowserWindow(QWidget):
    def __init__(self):
        super().__init__()
        browser = QWebEngineView()
        browser.setUrl(QUrl('https://google.com'))
        navbar = Navigation(browser)
        urlbar = URLTab()
        toolbar = Toolbar(navbar,urlbar)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        layout.addWidget(toolbar)
        layout.addWidget(browser)
