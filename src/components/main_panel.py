
from PyQt5.QtWidgets import QFrame, QGridLayout
from .server_output_box import ServerOutputBox

class MainPanel(QFrame):
    def __init__(self, parent=None, servers={}, others={}):
        super().__init__(parent)
        self.servers = servers
        self.others = others
        self.layout = QGridLayout()
        self.layout.setSpacing(5)
        self.layout.columnStretch(1)
        self.layout.rowStretch(1)
        self.layout.rowMinimumHeight(50)
        self.layout.columnMinimumWidth(50)
        self.setLayout(self.layout)
        self.serversOutputBoxes = []
        self.putServerWindows()
    
    def putServerWindows(self):
        row = 0
        col = 0
        for serverName in self.servers:
            outputBox = ServerOutputBox(self, serverName)
            self.serversOutputBoxes.append(outputBox)
            self.layout.addWidget(outputBox, row, col)
            col += 1
            if col == 3:
                row += 1
                col = 0

