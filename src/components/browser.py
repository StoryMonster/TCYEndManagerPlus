from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QWebEngineView):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.name = name

    def openUrl(self, url):
        self.load(QUrl(url))
    
    def getName(self):
        return self.name