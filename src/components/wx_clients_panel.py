
from PyQt5.QtWidgets import QFrame, QHBoxLayout
from .browser import Browser
from .wx_clients_display_panel import WxClientsDisplayPanel
from .wx_clients_ctrl_panel import WxClientsCtrlPanel
import sys


class WxClientsPanel(QFrame):
    def __init__(self, parent=None, wxclients={}):
        super().__init__(parent)
        self.wxclients = wxclients
        self.browsers = [Browser(self) for _ in range(6)]
        self.ctrlPanel = WxClientsCtrlPanel(self, wxclients, runAllClients=self.runAllClients)
        self.dispPanel = WxClientsDisplayPanel(self, self.browsers)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.ctrlPanel)
        self.layout.addWidget(self.dispPanel)
        self.layout.setStretchFactor(self.ctrlPanel, 1)
        self.layout.setStretchFactor(self.dispPanel, 5)
        self.setLayout(self.layout)
    
    def runAllClients(self, urls):
        for i in range(len(urls)):
            self.browsers[i].openUrl(urls[i])
