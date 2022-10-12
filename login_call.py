import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from login import Ui_Form

class MyMainForm(QMainWindow,Ui_Form):
    def __init__(self,parent=None):
        super(MyMainForm,self).__init__(parent)
        self.setupUi(self)
        # 添加登录按钮信号和槽。注意display函数不加小括号()
        self.login_Button.clicked.connect(self.display)
        # 添加退出按钮信号和槽。调用close函数
        self.cancel_Button.clicked.connect(self.close)
    def display(self):
        #利用line Edit控件对象text()函数获取界面输入
        username = self.user_lineEdit.text()
        password = self.pwd_lineEdit.text()
        #利用text Browser控件对象setText()函数设置界面显示
        self.user_textBrowser.setText("登录成功!\n" + "用户名是: "+ username+ ",密码是： "+ password)
if __name__ =="__main__":
    app=QApplication(sys.argv)
    myWin=MyMainForm()
    myWin.show()
    sys.exit(app.exec_())