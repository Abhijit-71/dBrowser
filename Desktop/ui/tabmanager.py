from PyQt6.QtWidgets import QWidget, QTabWidget, QHBoxLayout, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt

class TabManager(QWidget):
    def __init__(self, color="#1a1a1a"):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        
        
        self.add_tab_btn = QPushButton("+")
        self.add_tab_btn.setFixedSize(30, 30)
        self.add_tab_btn.setStyleSheet("""
            QPushButton {
                background-color: #2c3e50;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
            QPushButton:pressed {
                background-color: #3d5a6b;
            }
        """)
        self.add_tab_btn.clicked.connect(self.add_new_tab)
        self.tabs.setCornerWidget(self.add_tab_btn, Qt.Corner.TopRightCorner)
        
        layout.addWidget(self.tabs)
        self.setStyleSheet(f"background-color: {color};")
    
    def add_new_tab(self, url=None, label="New Tab"):
        """Add a new tab - to be implemented by user"""
       
        pass
    
    def close_tab(self, index):
        """Close a tab"""
        if self.tabs.count() > 1:
            widget = self.tabs.widget(index)
            self.tabs.removeTab(index)
            widget.deleteLater()