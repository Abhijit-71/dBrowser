from PyQt6.QtWebEngineCore import QWebEngineProfile , QWebEngineDownloadRequest 
from PyQt6.QtWidgets import QFileDialog

class Browser:

    _download_handler_connected = False

    def __init__(self):
        super().__init__()
        #self._download_handler_connected = False
        self.configure()
    
    def configure(self):
        self.profile = QWebEngineProfile.defaultProfile()
        self.profile.setPersistentCookiesPolicy(               #type:ignore
            QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies
        )

        if self._download_handler_connected == False:
            self.profile.downloadRequested.connect(lambda x:self.download_req(x)) #type:ignore
            self._download_handler_connected = True

        #return profile
    


    def download_req(self,download:QWebEngineDownloadRequest):
        
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
    
#https://www.svgrepo.com/svg/535115/alien