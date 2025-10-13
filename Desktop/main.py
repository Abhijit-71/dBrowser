from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication , QMainWindow , QVBoxLayout
from PyQt6.QtCore import QUrl
from ui.mwindow import MainWindow , PaddedWindow
from ui.toolbar import Navigation , Toolbar , URLTab
import sys
from ui.tabbar import TabManager
from ui.browser import BrowserWindow

"""app = QApplication(sys.argv)
browser = QWebEngineView()
browser.setUrl(QUrl('https://google.com'))

tools = Navigation(browser)
navbar = Toolbar(tools)
boom = PaddedWindow(browser,navbar)
window = MainWindow(boom)



window.show()
app.exec()"""

app = QApplication(sys.argv)


tab_manager = TabManager()
CentralWidget = PaddedWindow(tab_manager,"#181826")

# Create main window with blue title bar
window = MainWindow(CentralWidget,tab_manager)


window.show()
sys.exit(app.exec())
