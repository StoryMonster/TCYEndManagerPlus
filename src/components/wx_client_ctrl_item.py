
from PyQt5.QtWidgets import QCheckBox, QLineEdit, QLabel, QFrame, QHBoxLayout

class WxClientCtrlItem(QFrame):
    def __init__(self, parent=None, title="", text=""):
        super().__init__(parent)
        self.cbButton = QCheckBox(self)
        self.lblTitle = QLabel(self)
        self.editBox = QLineEdit(self)
        self.editBox.setMaxLength(32)
        self.editBox.setText(text)
        self.lblTitle.setText(title)
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.layout.addWidget(self.cbButton)
        self.layout.addWidget(self.lblTitle)
        self.layout.addWidget(self.editBox)

    def setSelected(self, isSelected):
        self.cbButton.setChecked(isSelected)

    def getUrl(self):
        return self.editBox.displayText()
    
    def isSelected(self):
        return self.cbButton.isChecked()