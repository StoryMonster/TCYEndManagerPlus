
from PyQt5.QtWidgets import QFrame, QGridLayout, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton
from .browser import Browser
from .wx_client_ctrl_item import WxClientCtrlItem

class WxClientsCtrlPanel(QFrame):
    def __init__(self, parent=None, wxclients={}, **callbacks):
        super().__init__(parent)
        self.wxclients = wxclients
        self.callbacks = callbacks
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        self.clientCtrlItems = []
        for wxclient in self.wxclients:
            item = WxClientCtrlItem(self, wxclient, self.wxclients[wxclient]["url"])
            self.clientCtrlItems.append(item)
        for i in range(len(self.wxclients), 6):
            item = WxClientCtrlItem(self, f"wx_client{i+1}", "")
            self.clientCtrlItems.append(item)
        self.logArea = QTextEdit(self)
        self.logArea.setReadOnly(True)
        self.btnRunAll = QPushButton(self)
        self.btnClearLog = QPushButton(self)
        self.btnClearLog.setText("清空日志")
        self.btnClearLog.clicked.connect(self.onClickedClearLog)
        self.btnRunAll.setText("一键运行")
        self.btnRunAll.clicked.connect(self.onClickedRunAll)
        self.putComponents()
    
    def putComponents(self):
        for item in self.clientCtrlItems:
            self.layout.addWidget(item)
        self.layout.addWidget(self.btnRunAll)
        self.layout.addWidget(self.btnClearLog)
        self.layout.addWidget(self.logArea)
        self.layout.setStretchFactor(self.logArea, 10)

    def log(self, content):
        self.logArea.append(content)

    def onClickedRunAll(self):
        urls = []
        for item in self.clientCtrlItems:
            url =  item.getUrl()
            if url.strip() != "":
                item.setSelected(True)
                urls.append(url)
        if "runAllClients" in self.callbacks:
            self.callbacks["runAllClients"](urls)

    def onClickedStopAll(self):
        for item in self.clientCtrlItems:
            item.setSelected(False)
        if "stopAllClients" in self.callbacks:
            self.callbacks["stopAllClients"]()

    def onClickedClearLog(self):
        self.logArea.clear()
        

class WxClientsDisplayPanel(QFrame):
    def __init__(self, parent=None, wxclients={}, browsers={}):
        super().__init__(parent)
        self.wxclients = wxclients
        self.browsers = browsers
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(5)
        row = 0
        col = 0
        for browser in self.browsers:
            self.layout.addWidget(browser, row, col)
            col += 1
            if col == 2:
                row += 1
                col = 0


class WxClientsPanel(QFrame):
    def __init__(self, parent=None, wxclients={}):
        super().__init__(parent)
        self.wxclients = wxclients
        self.browsers = [Browser(self) for _ in range(6)]
        self.ctrlPanel = WxClientsCtrlPanel(self, wxclients, runAllClients=self.runAllClients)
        self.dispPanel = WxClientsDisplayPanel(self, wxclients, self.browsers)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.ctrlPanel)
        self.layout.addWidget(self.dispPanel)
        self.layout.setStretchFactor(self.ctrlPanel, 1)
        self.layout.setStretchFactor(self.dispPanel, 5)
        self.setLayout(self.layout)
    
    def runAllClients(self, urls):
        for i in range(min(len(urls), len(self.browsers))):
            self.browsers[i].openUrl(urls[i])
