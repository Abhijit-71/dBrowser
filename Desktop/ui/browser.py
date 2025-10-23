from PyQt6.QtWidgets import QWidget , QVBoxLayout
from .toolbar import Toolbar , Navigation , URLTab
from PyQt6.QtCore import Qt , QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView 
from PyQt6.QtWebEngineCore import QWebEnginePage , QWebEngineProfile
import os , uuid
from .coreui import ProgressBar




class BrowserWindow(QWidget):
    
    #_shared_profile = None #works as  cache

    def __init__(self):
        super().__init__()

        
        #self._shared_profile = self._get_profile_data()

        
          
        self.browser = QWebEngineView()
        #browser.setPage(QWebEnginePage(self._shared_profile, browser))
        self.browser.setUrl(QUrl('https://google.com'))


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
    
    
    def _get_profile_data(self): #earlier all shared same profile and persistent storage
        unique_name = uuid.uuid4().hex
        profile_path = os.path.join(os.getcwd(),unique_name)
        cache_path = os.path.join(os.getcwd(),"user_cache")
        os.makedirs(profile_path, exist_ok=True)
        os.makedirs(cache_path, exist_ok=True)
        profile = QWebEngineProfile(unique_name)
        profile.setPersistentStoragePath(profile_path)
        profile.setCachePath(cache_path)
        profile.setPersistentCookiesPolicy(
            QWebEngineProfile.PersistentCookiesPolicy.ForcePersistentCookies
            )
        return profile