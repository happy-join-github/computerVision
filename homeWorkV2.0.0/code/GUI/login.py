import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton, QLabel,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox,
                             QMainWindow)
from PyQt5.QtCore import Qt
import pymysql
from reg import RegisterWindow
from share import SI
from mainUI import MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建用户名和密码标签和输入框
        user_label = QLabel('用户名:')
        self.user_input = QLineEdit()
        pass_label = QLabel('密码:')
        self.pass_input = QLineEdit()
        self.pass_input.setEchoMode(QLineEdit.Password)

        # 创建登录和注册按钮
        login_button = QPushButton('登录')
        register_button = QPushButton('注册')

        # 设置布局
        grid_layout = QGridLayout()
        grid_layout.addWidget(user_label, 0, 0)
        grid_layout.addWidget(self.user_input, 0, 1)
        grid_layout.addWidget(pass_label, 1, 0)
        grid_layout.addWidget(self.pass_input, 1, 1)

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(login_button)
        hbox_layout.addWidget(register_button)

        vbox_layout = QVBoxLayout()
        vbox_layout.addLayout(grid_layout)
        vbox_layout.addLayout(hbox_layout)

        self.setLayout(vbox_layout)

        # 设置窗口属性
        self.setWindowTitle('登录窗口')
        self.setGeometry(1000, 600, 400, 400)

        # 连接按钮的点击事件
        login_button.clicked.connect(self.login)
        register_button.clicked.connect(self.register)

    def login(self):
        # 获取用户输入的用户名和密码
        username = self.user_input.text()
        password = self.pass_input.text()

        with SI.connection.cursor() as cursor:
            # 执行SQL查询
            sql = "SELECT * FROM manage WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            if result:
                QMessageBox.warning(self, '登录成功', '用户名和密码正确，成功登录')
                SI.mainWin = MainWindow()
                SI.mainWin.show()
                self.hide()
            else:
                QMessageBox.warning(self, '登录失败', '用户名或密码错误')
                self.user_input.setText('')
                self.pass_input.setText('')

    def register(self):
        self.hide()
        SI.registerWin = RegisterWindow()
        SI.registerWin.show()
