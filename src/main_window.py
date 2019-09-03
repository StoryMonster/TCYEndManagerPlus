from PyQt5.QtWidgets import QMainWindow
from components.wx_clients_panel import WxClientsPanel


class MainWindow(QMainWindow):
    def __init__(self, parent=None, title="", wxclients={}):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.wxClientsPanel = WxClientsPanel(self, wxclients)
        self.setCentralWidget(self.wxClientsPanel)
        self.showMaximized()