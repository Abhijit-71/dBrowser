from PyQt6.QtWidgets import QWidget , QVBoxLayout
from .toolbar import Toolbar , Navigation , URLTab
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView 
from .coreui import ProgressBar
from browser.filter import FilterPage
from core.utils import resource_path
import os


# ================= Instance management are crucial !!!! ======================

class BrowserWindow(QWidget):
    
    _profile = None # works as  cache

    def __init__(self,browser_instance,tabmanager=None):

        super().__init__()

        
        if self._profile is None:
            self._profile = browser_instance.profile  # browser_instance  is Browser class having all profile related configs
        
        self.tab_manager = tabmanager
        self.browser = QWebEngineView()
        self.filtered_page = FilterPage(self._profile, self.browser)
        self.browser.setPage(self.filtered_page)
        html_path = resource_path("ui/index.html") # gets location for html file
        file_url = QUrl.fromLocalFile(html_path) # converts loaction to url
        self.browser.setUrl(file_url)

        self.browser.createWindow = self.create_window  #type:ignore


        progress = ProgressBar() 
        self.browser.loadStarted.connect(progress.on_load_started)
        self.browser.loadProgress.connect(progress.on_load_progress)
        self.browser.loadFinished.connect(progress.on_load_finished)

        
        navbar = Navigation(self.browser)
        self.urlbar = URLTab(self.browser)
        self.toolbar = Toolbar(navbar,self.urlbar)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.toolbar)
        layout.addWidget(progress)
        layout.addWidget(self.browser)

        self.browser.urlChanged.connect(self.update_urlbox)

    def update_urlbox(self,url):
        self.urlbar.urlbox.setText(url.toString())
    
    def create_window(self, window_type):
        new_tab = self.tab_manager.add_tab() if self.tab_manager else None
        return new_tab.browser if new_tab else None