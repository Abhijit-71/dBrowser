from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication , QMainWindow , QVBoxLayout
from PyQt6.QtCore import QUrl
from ui.mwindow import MainWindow , PaddedWindow
from ui.toolbar import Navigation , Toolbar
import sys
from ui.tabmanager import TabManager


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

browser = QWebEngineView()
browser.setUrl(QUrl('https://google.com'))

# Create navigation with dark gray background
tools = Navigation(browser, color="#34495e")

# Create toolbar with slightly lighter background
navbar = Toolbar(tools, color="#2c3e50")

# Create padded window with dark background
tab = TabManager()
boom = PaddedWindow(browser, navbar,tab, color="#151a20")

# Create main window with blue title bar
window = MainWindow(boom)

window.show()
sys.exit(app.exec())
