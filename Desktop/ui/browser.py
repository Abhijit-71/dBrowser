from PyQt6.QtWidgets import QWidget , QVBoxLayout
from .toolbar import Toolbar , Navigation , URLTab
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView 
from PyQt6.QtWebEngineCore import QWebEnginePage
from browser.corebrowser import Browser
from .coreui import ProgressBar

import os


class BrowserWindow(QWidget):
    
    _profile = None #works as  cache

    def __init__(self):
        super().__init__()

        
        if self._profile is None:
            self._profile = Browser().profile
        
          
        self.browser = QWebEngineView()
        self.browser.setPage(QWebEnginePage(self._profile, self.browser))
        #self.browser.setUrl(QUrl('https://google.com'))
        html_path = os.path.join(os.getcwd(),"ui/index.html")
        file_url = QUrl.fromLocalFile(html_path)
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
    
    
    """def _create_shared_profile(self): #earlier all shared same profile and persistent storage
        profile_path = os.path.join(os.getcwd(),"user_data")
        cache_path = os.path.join(os.getcwd(),"user_cache")
        os.makedirs(profile_path, exist_ok=True)
        os.makedirs(cache_path, exist_ok=True)
        profile = QWebEngineProfile.defaultProfile()    #("user_data")
        profile.setPersistentStoragePath(profile_path)
        profile.setCachePath(cache_path)
        profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.MemoryHttpCache)
        profile.setPersistentCookiesPolicy(
            QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies
            )
        return profile"""