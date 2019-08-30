
from PyQt5.QtWidgets import QFrame, QGridLayout
from .browser import Browser

class WxClientsPanel(QFrame):
    def __init__(self, parent=None, wxclients={}):
        super().__init__(parent)
        self.wxclients = wxclients
        self.browsers = []
        for name in wxclients:
            self.browsers.append(Browser(self, name))
        self.layout = QGridLayout()
        self.layout.setSpacing(5)
        self.layout.columnStretch(1)
        self.layout.rowStretch(1)
        self.layout.rowMinimumHeight(50)
        self.layout.columnMinimumWidth(50)
        self.setLayout(self.layout)
        self.putBrowsers()
        self.runAllBrowsers()
    
    def runAllBrowsers(self):
        for browser in self.browsers:
            print("fuck: " + self.wxclients[browser.getName()]["url"])
            browser.openUrl(self.wxclients[browser.getName()]["url"])

    def putBrowsers(self):
        row = 0
        col = 0
        for i in range(len(self.browsers)):
            self.layout.addWidget(self.browsers[i], row, col)
            col += 1
            if col == 2:
                row += 1
                col = 0

        