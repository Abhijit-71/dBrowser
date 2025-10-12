from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout , QLineEdit , QSizePolicy
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt ,QSize
from .coreui import HoverButton , IconButton
from PyQt6.QtGui import QIcon , QPixmap

class Navigation(QWidget):
    def __init__(self, browser:QWebEngineView):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(15, 8, 15, 8)
        layout.setSpacing(8)

        self.back = IconButton('svg/back.svg', 25)
        self.back.clicked.connect(browser.back)
        layout.addWidget(self.back)

        self.forward = IconButton('svg/forward.svg', 25)
        self.forward.clicked.connect(browser.forward)
        layout.addWidget(self.forward)

        self.reload = IconButton('svg/reload.svg', 25)
        self.reload.clicked.connect(browser.reload)
        layout.addWidget(self.reload)

        self.setFixedHeight(45)


class URLTab(QWidget):
    def __init__(self,color="#256eff"):
        super().__init__()
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(8)
        layout.addStretch()

        self.sengine = QLabel()
        self.sengine.setPixmap(QPixmap('svg/google_logo.svg'))
        self.sengine.setFixedSize(30,30)
        self.sengine.setScaledContents(True)
        self.sengine.setStyleSheet("background: transparent;")

        layout.addWidget(self.sengine)

        self.urlbox = QLineEdit()
        self.urlbox.setFixedHeight(35)
        self.urlbox.setMinimumWidth(250)
        self.urlbox.setPlaceholderText("Search with google or enter url .....")
        line_style = """
            QLineEdit {
                background: rgba(255,255,255,0.1);
                color: #ffffff;
                border: 1px solid rgba(255,255,255,0.06);
                padding: 10px 6px;
                border-radius: 4px;
            }
            QLineEdit:focus {
                border: 1px solid #6aaaff;
                background: rgba(255,255,255,0.02);
            }
            QLineEdit::placeholder {
                color: rgba(255,255,255,0.6);
            }
        """
        self.urlbox.setStyleSheet(line_style)
        self.urlbox.setSizePolicy(QSizePolicy.Policy.Expanding , QSizePolicy.Policy.Fixed)
        layout.addWidget(self.urlbox,1)
        self.setStyleSheet(f"background-color: {color};")
        self.setFixedHeight(45)



class Toolbar(QWidget):
    def __init__(self, navbar, urltab, color="#47327D"):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(50)
        layout.addWidget(navbar)
        layout.addWidget(urltab)
        layout.addStretch()
        
        self.setStyleSheet(f"background-color: {color};border-radius: 0px;border-top-right-radius: 8px;")
        self.setFixedHeight(45)
        
