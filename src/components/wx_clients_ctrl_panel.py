from PyQt5.QtWidgets import QFrame, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
from .wx_client_ctrl_item import WxClientCtrlItem


notice = """
<!doctype>
<html>
<head>
</head>
<body>
<p>请将下述代码拷贝到工程下文件userdef.js中，并做相应修改<br>
<pre>
<code>
const user_pwds = [
    {userName: "", password:"", nickName: ""},
    {userName: "", password:"", nickName: ""},
    {userName: "", password:"", nickName: ""},
    {userName: "", password:"", nickName: ""},
    {userName: "", password:"", nickName: ""}
]

if (typeof wx == 'undefined') {
    function GetUrlParam() {
        let url = document.location.toString();
        let arrUrl = url.split("?");
        let param = arrUrl[1];
        return param;
    }

    let userindex = GetUrlParam()
    if (typeof(userindex) != "undefined") {
        let index = Number(userindex);
        if (index &gt;= 0 && index &lt;= user_pwds.length) {
            userdef.userName = user_pwds[index].userName;
            userdef.password = user_pwds[index].password;
            userdef.nickName = user_pwds[index].nickName;
        }
    }
}
</code>
</pre>
</body>
</html>
"""

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
        self.logArea = QTextEdit(self)
        self.logArea.setReadOnly(True)
        self.btnRunAll = QPushButton(self)
        self.btnClearLog = QPushButton(self)
        self.btnClearLog.setText("清空日志")
        self.btnClearLog.clicked.connect(self.onClickedClearLog)
        self.btnRunAll.setText("一键运行")
        self.btnRunAll.clicked.connect(self.onClickedRunAll)
        self.putComponents()
        self.logArea.setHtml(notice)
    
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
            if not item.isSelected(): continue
            url =  item.getUrl()
            if url.strip() != "":
                urls.append(url)
            else:
                QMessageBox.information(None, "错误", f"{item.lblTitle.text()} 地址为空", QMessageBox.Yes)
                return
        if "runAllClients" in self.callbacks:
            self.callbacks["runAllClients"](urls)

    def onClickedClearLog(self):
        self.logArea.clear()