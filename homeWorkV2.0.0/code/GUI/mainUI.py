import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGridLayout, \
    QFileDialog, QMessageBox
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QPixmap, QFont
from share import SI


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.img_path = ''
    
    def update_time(self):
        current_time = self.time()
        self.time_label.setText(current_time)
    
    def time(self):
        now = QDateTime.currentDateTime()
        weekday = now.toString("ddd")
        date = now.toString("yyyy年MM月dd日")
        time = now.toString("HH时mm分ss秒")
        return f"{date}\n{weekday} {time}"
    
    def check_carer(self):
        with SI.connection.cursor() as cursor:
            sql = "select count(*) from carer where state=1"
            cursor.execute(sql)
            result = cursor.fetchone()
            return str(100 - result[0])
    def choose_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择图片", "../../dataset/shiyan/img/",
                                                   "图片文件 (*.png *.jpg *.jpeg *.bmp);;所有文件 (*)", options=options)
        if file_name:
            self.img_path = file_name
            pixmap = QPixmap(file_name)
            self.showImg.setPixmap(pixmap.scaled(self.showImg.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def total_money(self, s_t, e_t):
        # 计算时间间隔
        time_diff = e_t - s_t
        hours = time_diff.seconds // 3600
        minutes = (time_diff.seconds % 3600) // 60
    
        # 计算费用
        if hours == 0:
            money = 0
        elif 2 <= hours <= 3:
            if minutes != 0:
                money = (hours + 1) * 0.5
            else:
                money = hours * 0.5
        elif 4 <= hours <= 10:
            if minutes != 0:
                money = hours + 1
            else:
                money = hours
    
        else:
            if minutes != 0:
                money = (hours + 1) * 1.5
            else:
                money = hours * 1.5
        text = f'{s_t}\n进入车库,共使用{hours}小时{minutes}分钟\n收费{money}元'
        return money, text
    
    def check_car(self,lince):
        from datetime import datetime
        with SI.connection.cursor() as cursor:
            sql = "select * from carer where plateLince=%s"
            cursor.execute(sql,(lince,))
            result = cursor.fetchone()
            if result:
                new_state = 1
                start_time = result[1]
                end_time = datetime.now()
                money, text = self.total_money(start_time, end_time)
                self.info.setText(text)
                sql = """UPDATE carer SET state = %s,endTime=%s,money=%s
                                        WHERE plateLince = %s"""
                cursor.execute(sql, (new_state, end_time, money,lince))
                SI.connection.commit()
            else:
                sql = """INSERT INTO carer (startTime, endTime, plateLince, money, state)
                                         VALUES (%s, %s, %s, %s, %s)"""
    
                # 准备数据
                start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute(sql, (start_time, end_time, lince, 0, 0))
                SI.connection.commit()
                self.info.setText(f'欢迎{lince}用户\n{end_time}进入车库')
            
            cursor.close()
    
    def check_plackSpace(self):
        with SI.connection.cursor() as cursor:
            sql = 'select count(*) from carer where state=0'
            cursor.execute(sql)
            num = 100-cursor.fetchone()[0]
            self.carlabel.setText(f'剩余车位\n{num}')
        cursor.close()
        
    def check(self):
        if self.img_path != '':
            from ultralytics import YOLO
            import cv2
            import numpy as np
            # 保证ocr初始化唯一
            import os
            os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
            # Load a model
            model = YOLO("../runs/detect/train/weights/best.pt")
            results = model([self.img_path])
            boxes = results[0].boxes.xyxy.numpy()[0]
            x1, y1 = [int(np.floor(item)) for item in boxes[:2]]
            x2, y2 = [int(np.floor(item)) for item in boxes[2:]]
            img = cv2.imread(self.img_path)[y1:y2, x1:x2]
            from paddleocr import PaddleOCR
            ocr = PaddleOCR()
            plate_lince = ocr.ocr(img, cls=True)[0][0][1][0]
            plate_lince = plate_lince.replace('·', ' ')
            
            # 更新信息，检测车辆状态
            self.check_car(plate_lince)
            # TODO
            # 更新车位数
            self.check_plackSpace()
        else:
            QMessageBox.warning(self, '警告', '请选择图片')
    def initUI(self):
        self.setWindowTitle("智能停车场")
        self.setGeometry(600, 200, 1400, 1000)
        
        self.time_label = QLabel("当前时间")
        self.time_label.setFont(QFont("Arial", 12))
        self.time_label.setStyleSheet('background-color: #a0c5ff; color: black')
        self.time_label.setAlignment(Qt.AlignCenter)
        
        self.carlabel = QLabel("剩余车位: " + self.check_carer())
        self.carlabel.setFont(QFont("Arial", 12))
        self.carlabel.setStyleSheet('background-color: #70ffa9; color: black')
        self.carlabel.setAlignment(Qt.AlignCenter)
        
        self.info = QLabel("欢迎")
        self.info.setFont(QFont("Arial", 12))
        self.info.setStyleSheet('background-color: #ff00ff; color: black')
        self.info.setAlignment(Qt.AlignCenter)
        
        self.showImg = QLabel("图片显示区域")
        self.showImg.setFont(QFont("Arial", 12))
        self.showImg.setStyleSheet('background-color: white; color: black')
        self.showImg.setAlignment(Qt.AlignCenter)
        
        self.preferential = QLabel('今日优惠\n前三十分钟免费,0.5-4时0.5元/时 5-11时1元/时 12以上1.5元/时')
        self.preferential.setFont(QFont("Arial", 12))
        self.preferential.setStyleSheet('background-color: #a1f0ff; color: black')
        self.preferential.setAlignment(Qt.AlignCenter)
        
        self.btn1 = QPushButton('拍摄车牌')
        self.btn1.clicked.connect(self.choose_image)
        self.btn2 = QPushButton('视频检测')
        self.btn3 = QPushButton('开始检测')
        self.btn3.clicked.connect(self.check)
        
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.btn1)
        hlayout.addWidget(self.btn2)
        hlayout.addWidget(self.btn3)

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.time_label, 0, 0, 1, 1)
        grid_layout.addWidget(self.carlabel, 0, 1, 1, 1)
        grid_layout.addWidget(self.info, 1, 0, 1, 2)
        grid_layout.addWidget(self.showImg, 0, 2, 2, 1)
        grid_layout.addWidget(self.preferential,2,0,1,2)
        grid_layout.addLayout(hlayout,2,2,1,1)
        
        # 设置窗口布局
        self.setLayout(grid_layout)
        
        # Update time every second
        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)
