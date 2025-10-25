from PyQt6.QtWidgets import QWidget , QVBoxLayout
from .toolbar import Toolbar , Navigation , URLTab
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView 
from PyQt6.QtWebEngineCore import QWebEnginePage
from .coreui import ProgressBar
import os


class BrowserWindow(QWidget):
    
    _profile = None # works as  cache

    def __init__(self,browser_instance):
        super().__init__()

        
        if self._profile is None:
            self._profile = browser_instance.profile  # browser_instance  is Browser class having all profile related configs
        
          
        self.browser = QWebEngineView()
        self.browser.setPage(QWebEnginePage(self._profile, self.browser))
        html_path = os.path.join(os.getcwd(),"ui/index.html") # gets location for html file
        file_url = QUrl.fromLocalFile(html_path) # converts loaction to url
        self.browser.setUrl(file_url)


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
    
