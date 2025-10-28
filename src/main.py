from PyQt6.QtWidgets import QApplication
from ui.mwindow import MainWindow , PaddedWindow
import sys
from ui.tabbar import TabManager


# ======== starting point ==========

app = QApplication(sys.argv)


tab_manager = TabManager()
CentralWidget = PaddedWindow(tab_manager,"#181826")

# Create main window with custom title bar
window = MainWindow(CentralWidget,tab_manager)


window.show()
sys.exit(app.exec())
