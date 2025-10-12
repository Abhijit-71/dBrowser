from PyQt6.QtWidgets import (QWidget, QTabWidget, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QTabBar,QLineEdit, QDateEdit,QFormLayout)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon
from .browser import BrowserWindow

class TabManager(QWidget):
    def __init__(self):
        super().__init__()
        
        self.index = 1

        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(10)

        #tabBar
        self.TabBar = QTabWidget()
        self.TabBar.setTabsClosable(True)
        self.TabBar.setMovable(True)
        self.TabBar.setDocumentMode(True)
        self.TabBar.setContentsMargins(0,0,0,0)
        self.TabBar.setStyleSheet("""
            QTabWidget::pane {
                border: none;
                background: transparent;
                
            }
            QTabBar {
                background: transparent;
            }
            QTabBar::tab {
                background: #47327D;
                color: #ffffff;
                padding: 8px 0px 6px 0px;
                margin-right: 3px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
                min-width: 100px;
            }
            QTabBar::tab:selected {
                background: #B65FCF;
            }
            QTabBar::tab:hover {
                background: #9a6dbe;
            }
            QTabBar::tab:selected:hover {
                background: #9a6dbe;
            }
            QTabBar::close-button {
                border-image: url("svg/cross.svg") 0 0 0 0 round round;

            }
        """)

        
        self.TabBar.tabBar().setFixedWidth(500) # type: ignore 
        self.plus_btn = QPushButton("+")
        self.plus_btn.setFixedSize(30, 30)
        #self.setStyleSheet("background: #fff;")
        self.plus_btn.clicked.connect(self.add_tab)

        layout.addWidget(self.plus_btn)
        layout.addWidget(self.TabBar)
        
        self.setLayout(layout)
        
        self.TabBar.addTab(BrowserWindow(),"browser")
        self.TabBar.tabCloseRequested.connect(self.close_tab)
        
    def add_tab(self):
            tab_content = BrowserWindow()
            index = self.TabBar.addTab(tab_content, f"Tab {self.index}")
            self.TabBar.setCurrentIndex(index)
            self.index += 1 
    
        
        
    def close_tab(self, index):
        widget = self.TabBar.widget(index)
        if self.TabBar.count() <= 1:
            return
        self.TabBar.removeTab(index)
        
        if widget :
            widget.deleteLater()
    

        

        