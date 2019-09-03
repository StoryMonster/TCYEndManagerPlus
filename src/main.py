#! encoding=utf-8
import sys
from PyQt5.QtWidgets import QApplication
import PyQt5.sip
from main_window import MainWindow

if __name__ == "__main__":
    wxclients = {
        "client1": {"url": "http://localhost:7456?0"},
        "client2": {"url": "http://localhost:7456?1"},
        "client3": {"url": "http://localhost:7456?2"},
        "client4": {"url": "http://localhost:7456?3"},
        "client5": {"url": "http://localhost:7456?4"},
        "client6": {"url": "http://localhost:7456?5"},
    }
    app = QApplication([])
    window = MainWindow(None, "TCYWechatGameDevHelper", wxclients)
    window.show()
    sys.exit(app.exec_())
