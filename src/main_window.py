from PyQt5.QtWidgets import QMainWindow
from components.main_panel import MainPanel
from components.wx_clients_panel import WxClientsPanel


class MainWindow(QMainWindow):
    def __init__(self, parent=None, title="", servers={}, clients={}, wxclients={}, others={}):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.mainPanel = MainPanel(self, servers, others)
        #self.wxClientsPanel = WxClientsPanel(self, wxclients) if len(wxclients) > 0 else None
        #if self.wxClientsPanel:
        #    self.setCentralWidget(self.wxClientsPanel)
        