import sys

from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QMessageBox, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QGridLayout, QHBoxLayout
from share import SI
import pymysql


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('注册页面')
        self.setGeometry(1000, 600, 400, 400)

        # 创建用户名、密码和确认密码标签和输入框
        username_label = QLabel('用户名:')
        self.username_input = QLineEdit()
        password_label = QLabel('密码:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        confirm_password_label = QLabel('确认密码:')
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        # 创建注册和登录按钮
        register_button = QPushButton('注册')

        # 设置布局
        grid_layout = QGridLayout()
        grid_layout.addWidget(username_label, 0, 0)
        grid_layout.addWidget(self.username_input, 0, 1)
        grid_layout.addWidget(password_label, 1, 0)
        grid_layout.addWidget(self.password_input, 1, 1)
        grid_layout.addWidget(confirm_password_label, 2, 0)
        grid_layout.addWidget(self.confirm_password_input, 2, 1)

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(register_button)

        vbox_layout = QVBoxLayout()
        vbox_layout.addLayout(grid_layout)
        vbox_layout.addLayout(hbox_layout)

        self.setLayout(vbox_layout)

        # 连接按钮的点击事件
        register_button.clicked.connect(self.register)

    def register(self):
        # 获取用户输入的用户名和密码
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        # 检查密码和确认密码是否相同
        if password == confirm_password:
            try:
                # 创建游标对象
                with SI.connection.cursor() as cursor:
                    # 执行SQL插入操作
                    sql = "INSERT INTO manage(username, password) VALUES (%s, %s)"
                    cursor.execute(sql, (username, password))
                SI.connection.commit()
                QMessageBox.warning(self, '注册成功', f'用户名: {username}, 密码: {password} - 注册成功')
                SI.loginWin.show()
                self.close()
            except pymysql.Error as e:
                QMessageBox.warning(self, '注册失败', f'注册失败: {e}')
        else:
            QMessageBox.warning(self, '注册失败', '密码和确认密码不一致')
            self.password_input.setText('')
            self.confirm_password_input.setText('')
