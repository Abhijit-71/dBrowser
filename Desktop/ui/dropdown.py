from PyQt6.QtWidgets import (QMenu , QWidget , QVBoxLayout, QLabel , QHBoxLayout, QPushButton, 
    QListWidget, QListWidgetItem, QTableWidget, 
    QTableWidgetItem, QHeaderView,QProgressBar)

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon,QAction
from PyQt6.QtWebEngineCore import QWebEngineDownloadRequest

class DownloadTab(QWidget):
    def __init__(self,DownloadManager):
        super().__init__()

        main = QVBoxLayout()

        main.setContentsMargins(0,0,0,0)
        main.setSpacing(0)

        top_bar = QWidget()
        top_bar.setFixedHeight(45)
        top_bar.setStyleSheet("background-color: #47327D; border-radius: 0px; border-top-right-radius: 8px;")
        top_label = QHBoxLayout()
        top_label.setContentsMargins(40,10,0,10)
        top_label.addWidget(QLabel("Find all your Downloads here"))
        top_bar.setLayout(top_label)
        main.addWidget(top_bar)

        body = QWidget()
        body.setStyleSheet("background-color: #1e1e1e; border-radius: 0px; border-bottom-right-radius: 8px; border-bottom-left-radius: 8px;")
        download_inst_holder = QVBoxLayout()
        download_inst_holder.setContentsMargins(20,20,20,20)
        """card = DownloadManager
        card.setStyleSheet("background-color: #3e3e3e; border-radius: 8px;")"""
        download_inst_holder.addWidget(DownloadManager)
        body.setLayout(download_inst_holder)

        main.addWidget(body)
        self.setLayout(main)



class DownloadManager(QWidget):
    def __init__(self):
        super().__init__()
        self.downloads = []
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(10,10,10,10)
        layout.setSpacing(20)

        # Current downloads table
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["File","Progress","Status", "Actions"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch) #type:ignore

        self.table.verticalHeader().setDefaultSectionSize(80) #type:ignore
        self.table.verticalHeader().setVisible(False) #type:ignore
        
        current_label = QLabel("Current Downloads")
        current_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #ffffff; margin-bottom: 5px;")
        layout.addWidget(current_label)
        self.table.setStyleSheet("""
        QTableWidget {
            background-color: #2a2a2a;
            border: none;
            border-radius: 12px;
            gridline-color: #3a3a3a;
        }
        QTableWidget::item {
            padding: 10px;
            border-bottom: 1px solid #3a3a3a;
        }
        QHeaderView::section {
            background-color: #333333;
            color: #ffffff;
            padding: 10px;
            border: none;
            font-weight: bold;
        }
    """)
        layout.addWidget(self.table)

        # Recent downloads list
        recent_label = QLabel("Recent Downloads")
        recent_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #ffffff; margin-top: 10px; margin-bottom: 5px;")
        layout.addWidget(recent_label)
        self.recent_list = QListWidget()
        self.recent_list.setMaximumHeight(200)
        self.recent_list.setStyleSheet("""
        QListWidget {
            background-color: #2a2a2a;
            border: none;
            border-radius: 12px;
            padding: 10px;
        }
        QListWidget::item {
            padding: 12px;
            border-bottom: 1px solid #3a3a3a;
            color: #ffffff;
        }
        QListWidget::item:hover {
            background-color: #353535;
            border-radius: 6px;
        }
    """)
        layout.addWidget(self.recent_list)

        self.setLayout(layout)

    def add_download(self, download:QWebEngineDownloadRequest):
        filename = download.downloadFileName()
        row = 0
        self.table.insertRow(row)

        # File  and details
        details = QWidget()
        details.setStyleSheet("background:transparent")
        details_layout = QVBoxLayout()
        details_layout.addWidget(QLabel(filename))

        progress_bar = QProgressBar()
        progress_bar.setTextVisible(False)
        details_layout.addWidget(progress_bar)

        details.setLayout(details_layout)

        self.table.setCellWidget(row, 0, details)   

        

        progress_label = QTableWidgetItem(f"{(download.receivedBytes())/1024**2:.1f} MB/{(download.totalBytes())/1024**2:.1f} MB")
        progress_label.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table.setItem(row,1,progress_label)
        # Status
        status_item = QTableWidgetItem("Starting...")
        status_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.table.setItem(row, 2, status_item)

        # Pause/Resume button
        actions = QWidget()
        actions.setStyleSheet("background:transparent")

        actions_layout = QHBoxLayout()

        pause_btn = QPushButton("Pause")
        pause_btn.setEnabled(False)
        pause_btn.clicked.connect(lambda : self.toggle_pause(download,pause_btn))
        pause_btn.setStyleSheet("""
    QPushButton {
        background-color: #47327D;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #5a3f9e;
    }
    QPushButton:disabled {
        background-color: #2a2a2a;
        color: #666666;
    }
""")
        actions_layout.addWidget(pause_btn)

        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(download.cancel)
        cancel_btn.setStyleSheet("""
    QPushButton {
        background-color: #d32f2f;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #f44336;
    }
""")
        actions_layout.addWidget(cancel_btn)

        actions.setLayout(actions_layout)

        self.table.setCellWidget(row, 3, actions)

        

        # Connect signals
        download.receivedBytesChanged.connect(lambda: self.update_progress(download, progress_bar,progress_label))
        download.stateChanged.connect(lambda: self.update_status(download, status_item, pause_btn))
        download.isFinishedChanged.connect(lambda: self.finish_download(download, filename))


        # Start download
        download.accept()
        self.downloads.append(download.downloadFileName()) #filename
        print(self.downloads)

        
        
    def update_progress(self,download:QWebEngineDownloadRequest,progress_bar:QProgressBar,progress_label):
        print(download.receivedBytes())
        progress = (download.receivedBytes()/download.totalBytes())*100
        progress_bar.setValue(int(progress))
        progress_label.setText(f"{(download.receivedBytes())/1024**2:.1f} MB/{(download.totalBytes())/1024**2:.1f} MB")



    def toggle_pause(self, download: QWebEngineDownloadRequest, button: QPushButton):
        # toggle and update button text
        if button.text() == "Pause":
            download.pause()
            button.setText("Resume")
        else:
            download.resume()
            button.setText("Pause")


    def update_status(self, download, status_item, pause_btn):
        state = download.state()
        mapping = {
            download.DownloadState.DownloadRequested: "Requested",
            download.DownloadState.DownloadInProgress: "Downloading",
            download.DownloadState.DownloadCompleted: "Completed",
            download.DownloadState.DownloadCancelled: "Cancelled",
            download.DownloadState.DownloadInterrupted: "Failed",
        }
        status_item.setText(mapping.get(state, "Unknown"))

        # Handle pause/resume
        if state == download.DownloadState.DownloadInProgress:
            pause_btn.setEnabled(True)
            pause_btn.clicked.connect(lambda: self.toggle_pause)


    def finish_download(self, download, filename):
        if download.state() == download.DownloadState.DownloadCompleted:
            self.recent_list.insertItem(0,QListWidgetItem(f"{filename} - Completed ✅"))
        elif download.state() == download.DownloadState.DownloadInterrupted:
            self.recent_list.insertItem(0,QListWidgetItem(f"{filename} - Failed ❌"))
        elif download.state() == download.DownloadState.DownloadCancelled:
            self.recent_list.insertItem(0,QListWidgetItem(f"{filename} - Cancelled ⏹"))

#https://www.thinkbroadband.com/download   === test url


class MenuDrop(QMenu):
    def __init__(self):
        super().__init__()

        add_tab = QAction(QIcon("svg/home_tab.svg"),"Add New Tab",self)
        #add_tab.setStatusTip("Add New Tab")
        add_tab.setShortcut('Ctrl+T')
        self.addAction(add_tab)

        self.addSeparator()

        self.addAction(QIcon("svg/logo.svg"),"BookMark")
        self.addAction(QIcon("svg/logo.svg"),"History")
        self.addSeparator()
        
        print = QAction(QIcon("svg/home_tab.svg"),"Print",self)
        #print.setStatusTip("Print this page")
        print.setShortcut('Ctrl+P')
        self.addAction(print)

        save = QAction(QIcon("svg/home_tab.svg"),"Save Page As",self)
        #save.setStatusTip("Save this page")
        save.setShortcut('Ctrl+S')
        self.addAction(save)
        self.addSeparator()

        self.addAction(QIcon("svg/logo.svg"),"Settings")
        self.addAction(QIcon("svg/logo.svg"),"Help")
        self.addSeparator()
        
        exit = QAction(QIcon("svg/home_tab.svg"),"Exit",self)
        #exit.setStatusTip("Add New Tab")
        exit.setShortcut('Alt+F4')
        self.addAction(exit)

        self.setStyleSheet("""
            QMenu {
                background-color: #1e1e1e; 
                color: #f5f5f5;     
                border: 1px solid #444;
                padding: 10px;
                border-radius: 8px;
            }

            QMenu::item {
                padding: 6px 18px;
                border-radius: 4px;
            }

            QMenu::item:selected {
                background-color: #47327D; 
                color: white;
            }

            QMenu::separator {
                height: 1px;
                background: #555;
                margin: 4px 8px;
            }

            QMenu::icon {
                margin-right: 6px;
            }
        """)
        
