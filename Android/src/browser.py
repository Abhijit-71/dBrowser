#for webview widget from pyjnius

from kivy.uix.widget import Widget 


class Browser(Widget):
    def __init__(self):
      super().__init__()
      from jnius import autoclass
      PythonActivity = autoclass('org.kivy.android.PythonActivity')
      WebView = autoclass('android.webkit.WebView')
      WebViewClient = autoclass('android.webkit.WebViewClient')
      self.activity = PythonActivity.mActivity
      self.webview = WebView(self.activity)
      self.webview.getSettings().setJavaScriptEnabled(True)
      self.webview.setWebViewClient(WebViewClient())  # Stay inside the app
      self.webview.loadUrl("https://www.google.com")
      self.activity.setContentView(self.webview)



    
class demoBrowser():
    def __init__(self):
        from kivy.uix.label import Label
        self.webview = Label(text="not on android")
