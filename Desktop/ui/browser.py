from PyQt6.QtWidgets import QWidget , QVBoxLayout
from .toolbar import Toolbar , Navigation , URLTab
from PyQt6.QtCore import Qt , QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView 
from PyQt6.QtWebEngineCore import QWebEnginePage , QWebEngineProfile
import os
from .coreui import ProgressBar




class BrowserWindow(QWidget):
    
    _shared_profile = None #works as  cache

    def __init__(self):
        super().__init__()

        if self._shared_profile is None:
            self._shared_profile = self._get_profile_data()

        
          
        browser = QWebEngineView()

        progress = ProgressBar() 
        browser.loadStarted.connect(progress.on_load_started)
        browser.loadProgress.connect(progress.on_load_progress)
        browser.loadFinished.connect(progress.on_load_finished)

        browser.setPage(QWebEnginePage(self._shared_profile, browser))
        browser.setUrl(QUrl('https://google.com'))
        navbar = Navigation(browser)
        urlbar = URLTab()
        self.toolbar = Toolbar(navbar,urlbar)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        layout.addWidget(self.toolbar)
        layout.addWidget(progress)
        layout.addWidget(browser)
    
    def _get_profile_data(self):
        profile_path = os.path.join(os.getcwd(),"user_data")
        cache_path = os.path.join(os.getcwd(),"user_cache")
        os.makedirs(profile_path, exist_ok=True)
        os.makedirs(cache_path, exist_ok=True)
        profile = QWebEngineProfile("DefaultProfile")
        profile.setPersistentStoragePath(profile_path)
        profile.setCachePath(cache_path)
        profile.setPersistentCookiesPolicy(
            QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
            )
        return profile