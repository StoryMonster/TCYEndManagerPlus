from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)

    def openUrl(self, url):
        self.load(QUrl(url))