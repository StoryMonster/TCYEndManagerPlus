from PyQt5.QtWidgets import QFrame, QGridLayout

class WxClientsDisplayPanel(QFrame):
    def __init__(self, parent=None, browsers={}):
        super().__init__(parent)
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