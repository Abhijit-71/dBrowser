from PyQt6.QtWebEngineCore import QWebEngineProfile , QWebEngineDownloadRequest 
from PyQt6.QtWidgets import QFileDialog
import os

class Browser:

    _download_handler_connected = False

    def __init__(self):
        super().__init__()
        self.configure()
    
    def configure(self):


        """why this works ?? ==> Earlier , profile was instanciated many times creating multiple profiles , now only one profile 
         same name does not mean one profile . May also create many instaces of a profile"""
        

        profile_path = os.path.join(os.getcwd(),"user_data")
        cache_path = os.path.join(os.getcwd(),"user_cache")
        os.makedirs(profile_path, exist_ok=True)
        os.makedirs(cache_path, exist_ok=True)
        self.profile = QWebEngineProfile("user_data")
        self.profile.setPersistentStoragePath(profile_path)
        self.profile.setCachePath(cache_path)
        self.profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.MemoryHttpCache)
        self.profile.setPersistentCookiesPolicy(
            QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies
            )
        

        # download is also connected once , for no repeated signal

        if self._download_handler_connected == False:
            self.profile.downloadRequested.connect(self.download_req) #type:ignore
            self._download_handler_connected = True

        
    

    @staticmethod
    def download_req(download:QWebEngineDownloadRequest):
        
        suggested_name = download.downloadFileName()
    
        print(f"trigerred {suggested_name}")

        path,_ = QFileDialog.getSaveFileName(
            None,
            "dBrowser Download Manager",
            suggested_name,
        )

        if path:
            download.setDownloadFileName(path)
            download.accept()
        else:
            download.cancel()
            print("cancelled")
    

