
from PyQt5.QtWidgets import QPlainTextEdit


class ServerOutputBox(QPlainTextEdit):
    def __init__(self, parent, name):
        super().__init__(parent)
        self.name = name
        self.setReadOnly(True)

    def error(self, text):
        html = '<font color="red">[ERROR] ' + text + '</font><br>'
        self.appendHtml(html)
    
    def warn(self, text):
        html = '<font color="yellow">[WARN] ' + text + '</font><br>'
        self.appendHtml(html)

    def info(self, text):
        self.appendPlainText(text + "\n")