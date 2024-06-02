import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql


class UI:
    def __init__(self):
        # 开始自动启动登陆页面
        self.login_form(0)
        self.img_path =''
    
    def login_form(self, flag=0):
        if flag == 1:
            self.reg_frame.destroy()
        else:
            # 创建登录窗口
            self.log_form = tk.Tk()
            self.log_form.title('登录')
            
            # 计算屏幕宽度和高度
            screen_width = self.log_form.winfo_screenwidth()
            screen_height = self.log_form.winfo_screenheight()
            # 窗口宽度
            window_width = 400
            window_height = 400
            # 计算窗口位于屏幕中心的坐标
            center_x = int((screen_width - window_width) / 2)
            center_y = int((screen_height - window_height) / 2)
            self.log_form.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            
            # 加载背景图
            from PIL import Image, ImageTk
            # 加载背景图片
            background_image = Image.open("../../logBG.jpg")  # 使用Pillow打开图像
            background_image = background_image.resize((window_width, window_height), Image.LANCZOS)  # 调整图像大小
            background_image = ImageTk.PhotoImage(background_image)  # 转换为Tkinter兼容的格式
            
            # 创建一个Label组件，设置其图片属性为背景图片
            background_label = tk.Label(self.log_form, image=background_image)
            background_label.place(relwidth=1, relheight=1)  # 让标签大小适应窗口大小
            
            self.username = tk.StringVar()
            self.password = tk.StringVar()
            
            self.username_label = tk.Label(self.log_form, text='用户名:', font=('Arial', 18))
            self.username_label.place(x=70, y=80)
            
            self.username_entry = tk.Entry(self.log_form, textvariable=self.username)
            self.username_entry.place(x=160, y=85)
            
            self.password_label = tk.Label(self.log_form, text='密码:', font=('Arial', 18))
            self.password_label.place(x=70, y=120)
            
            self.password_entry = tk.Entry(self.log_form, textvariable=self.password, show='*')
            self.password_entry.place(x=160, y=128)
            
            self.login_button = tk.Button(self.log_form, text='登录', command=self.login, font=('Arial', 18))
            self.login_button.place(x=100, y=200)
            
            self.register_button = tk.Button(self.log_form, text='注册', command=self.register, font=('Arial', 18))
            self.register_button.place(x=200, y=200)
            
            self.log_form.mainloop()
    
    def login(self):
        username = self.username.get()
        Input_password = self.password.get()
        # 数据库连接
        db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '000000',
            'database': 'homework',
            'charset': 'utf8mb4'
        }
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('select password from manage where username=%s', (username,))
        password = cursor.fetchall()
        if password:
            # print(password[0][0],Input_password)
            if password[0][0] == Input_password:
                messagebox.showinfo('登录', '登录成功')
                cursor.close()
                conn.close()
                self.log_form.destroy()
                self.mainUI()
            else:
                messagebox.showinfo('登录', '密码错误')
        else:
            messagebox.showinfo('登录', '用户名不存在')
    
    def submit_mysql(self, name, password, entry_password):
        name = name.get()
        password = password.get()
        entry_password = entry_password.get()
        if password != entry_password:
            messagebox.showerror('注册', '两次密码不一致')
            return
        # 数据库连接
        db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '000000',
            'database': 'homework',
            'charset': 'utf8mb4'
        }
        
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('insert into manage(username,password) values(%s,%s)', (name, password))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo('注册', '注册成功')
    
    def register(self):
        # 停用的登录页面
        self.log_form.destroy()
        # 创建注册页面
        self.reg_frame = tk.Tk()
        self.reg_frame.title('注册')
        # 计算屏幕宽度和高度
        screen_width = self.reg_frame.winfo_screenwidth()
        screen_height = self.reg_frame.winfo_screenheight()
        # 窗口宽度
        window_width = 500
        window_height = 500
        # 计算窗口位于屏幕中心的坐标
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)
        self.reg_frame.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
        # 加载背景图
        from PIL import Image, ImageTk
        # 加载背景图片
        background_image = Image.open("../../regBG.jpg")  # 使用Pillow打开图像
        background_image = background_image.resize((window_width, window_height), Image.LANCZOS)  # 调整图像大小
        background_image = ImageTk.PhotoImage(background_image)  # 转换为Tkinter兼容的格式
        
        # 创建一个Label组件，设置其图片属性为背景图片
        background_label = tk.Label(self.reg_frame, image=background_image)
        background_label.place(relwidth=1, relheight=1)  # 让标签大小适应窗口大小
        
        username = tk.StringVar()
        password = tk.StringVar()
        entrypassword = tk.StringVar()
        
        username_label = tk.Label(self.reg_frame, text='用户名:', font=('Arial', 18))
        username_label.place(x=65, y=150)
        
        username_entry = tk.Entry(self.reg_frame, font=('Arial', 18), textvariable=username)
        username_entry.place(x=150, y=150)
        
        password_label = tk.Label(self.reg_frame, text='密码:', font=('Arial', 18))
        password_label.place(x=85, y=200)
        
        password_entry = tk.Entry(self.reg_frame, font=('Arial', 18), show='*', textvariable=password)
        password_entry.place(x=150, y=200)
        
        entrypassword_label = tk.Label(self.reg_frame, text='确认密码:', font=('Arial', 18))
        entrypassword_label.place(x=35, y=250)
        entry_password = tk.Entry(self.reg_frame, font=('Arial', 18), show='*', textvariable=entrypassword)
        entry_password.place(x=150, y=250)
        
        login_button = tk.Button(self.reg_frame, text='登录', font=('Arial', 18), command=lambda: self.login_form(1))
        login_button.place(x=100, y=320)
        
        reg_button = tk.Button(self.reg_frame, text='注册', font=('Arial', 18),
                               command=lambda: self.submit_mysql(username, password, entrypassword))
        reg_button.place(x=250, y=320)
        self.reg_frame.mainloop()

    def check_plackSpace(self):
        # 数据库连接
        import pymysql
        db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '000000',
            'database': 'homework',
            'charset': 'utf8mb4'
        }
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('select count(*) from history_user where state=0')
        num = 100 - cursor.fetchall()[0][0]
        Parking_space = tk.Label(self.main_form, text=f'剩余车位\n\n{num}', font=('Arial', 18), borderwidth=2,
                                 relief="groove",
                                 width=15, height=5, fg='#ff00ff')  # bg='#fff'
        Parking_space.place(x=50, y=100)
        # 关闭游标和连接
        cursor.close()
        conn.close()

    def took_picture(self):
        import cv2
        import datetime
        # 初始化摄像头
        cap = cv2.VideoCapture(0)
        # 获取当前时间并格式化文件名
        filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = filename.replace(":", "-")  # 替换冒号为连字符
        # 读取一帧
        ret, frame = cap.read()
        # 检查是否成功读取帧
        if ret:
            # 保存图片
            cv2.imwrite(f'../../images/{filename}.jpg', frame)
        else:
            print("Failed to read frame")
    
        # 释放摄像头
        cap.release()
        from PIL import Image, ImageTk
        import os
        img_name = os.listdir('../../img')[-1]
        self.img_path = f'../../img/{img_name}'
        image = Image.open(f"../../img/{img_name}")
    
        # 缩放图片到400x240像素
        image = image.resize((540, 360), Image.LANCZOS)
    
        # 将图片转换为PhotoImage对象
        photo = ImageTk.PhotoImage(image)
        img_label = tk.Label(self.img_label, image=photo)
        img_label.image = photo
        img_label.place(x=0, y=0)

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
        text = f'\n{s_t}\n进入车库,共使用{hours}小时{minutes}分钟\n收费{money}元'
        return money, text

    def check_car(self, lince):
        from datetime import datetime
        import pymysql
        db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': 'root',
            'password': '000000',
            'database': 'homework',
            'charset': 'utf8mb4'
        }
        # 已字典的形式返回 键是列名称 值是列值
        con = pymysql.connect(**db_config, cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        platelince = lince
        cur.execute("select * from history_user where platelince=%s", (platelince,))
        result = cur.fetchone()
        if result is None:
            # 准备SQL语句
            sql = """
                INSERT INTO history_user (start_time, end_time, platelince, money, state)
                VALUES (%s, %s, %s, %s, %s)
                """
        
            # 准备数据
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            end_time = datetime.now()
            money = 0
            state = 0
        
            # 执行SQL语句
            try:
                cur.execute(sql, (start_time, end_time, lince, money, state))
                con.commit()
                self.welcome.config(text=f'欢迎{lince}用户\n{start_time}进入车库')
                self.welcome.place(x=150, y=50)
            except Exception as e:
                print("插入数据失败", e)
                con.rollback()
        else:
            # 准备SQL语句
            sql = """
                UPDATE history_user
                SET state = %s,end_time=%s,money=%s
                WHERE platelince = %s
                """
        
            # 准备数据
            new_state = 1  # 假设您要将state更新为1
            end_time = datetime.now()
            money, text = self.total_money(result['start_time'], end_time)
        
            # 执行SQL语句
            try:
                cur.execute(sql, (new_state, end_time, money, lince))
                con.commit()
                self.welcome.config(text=lince + '用户' + text)
                self.welcome.place(x=0,y=10)
                #     展示付款码
                img = Image.open('../../WX.jpg')
                img = img.resize((300, 200), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                WX = tk.Label(self.info, image=photo)
                WX.image = photo
                WX.place(x=500, y=0)
        
            except Exception as e:
                messagebox.showerror('警告', '更新失败')
                con.rollback()
        # 关闭游标和连接
        cur.close()
        con.close()
    
    def mainUI(self):
        self.img_path = ''
        self.main_form = tk.Tk()
        self.main_form.title('车牌识别管理系统')
        # 计算屏幕宽度和高度
        screen_width = self.main_form.winfo_screenwidth()
        screen_height = self.main_form.winfo_screenheight()
        # 窗口宽度
        window_width = 900
        window_height = 850
        # 计算窗口位于屏幕中心的坐标
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)
        self.main_form.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        # 主页面
        
        # 优惠组件
        preferential = tk.Label(self.main_form, text='今日优惠', font=('Arial', 18))
        preferential.place(x=50, y=15)
        preferential_label = tk.Label(self.main_form, text='前三十分钟免费,0.5-4时0.5元/时 5-11时1元/时 12以上1.5元/时',
                                      font=('Arial', 18))
        preferential_label.place(x=50, y=50)

        # 时间组件
        def time_pro():
            import datetime
            now = datetime.datetime.now()
            weekend = now.weekday()  # 0-6 星期一:0
            weekend_dic = {0: '星期一', 1: '星期二', 2: '星期三', 3: '星期四', 4: '星期五', 5: '星期六', 6: '星期日'}
            w_s = weekend_dic[weekend]
    
            date, time = now.strftime("%Y-%m-%d %H:%M:%S").split(' ')
            date = date.split('-')
            date = date[0] + '年' + date[1] + '月' + date[2] + '日'
            time = time.split(':')
            time = time[0] + '时' + time[1] + '分' + time[2] + '秒'
            dataTime = date + ' ' + w_s + ' ' + time
            showTime = tk.Label(self.main_form, text=f'当前时间\n\n{dataTime}', width=40, height=5,
                                font=('Arial', 18), borderwidth=2, relief="groove")
            showTime.place(x=300, y=100)
            self.main_form.after(100, time_pro)
        # 剩余车位
        self.check_plackSpace()
        # 当前时间
        self.main_form.after(100, time_pro)
        # 出入信息
        self.info = tk.Frame(self.main_form, borderwidth=1, relief='solid', width=816, height=200, bg='#dadada')
        self.info.place(x=50, y=250)
        self.welcome = tk.Label(self.info, text='欢迎使用', font=('arial', 25), fg='#ff0000')
        self.welcome.place(x=0, y=5)
        # 图像显示部分
        self.img_label = tk.Frame(self.main_form, borderwidth=1, relief='solid', width=540, height=390)
        self.img_label.place(x=10, y=455)
        
        def check():
            if self.img_path!='':
                from ultralytics import YOLO
                import cv2
                import numpy as np
                # 保证ocr初始化唯一
                import os
                os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
                # Load a model
                model = YOLO("../runs/detect/train3/weights/best.pt")
                results = model([self.img_path])
                boxes = results[0].boxes.xyxy.numpy()[0]
                x1, y1 = [int(np.floor(item)) for item in boxes[:2]]
                x2, y2 = [int(np.floor(item)) for item in boxes[2:]]
                img = cv2.imread(self.img_path)[y1:y2, x1:x2]
                from paddleocr import PaddleOCR
                ocr = PaddleOCR()
                plate_lince = ocr.ocr(img, cls=True)[0][0][1][0]
                plate_label = tk.Label(self.img_label, text=plate_lince, font=25, bg='#ff00ff')
                plate_label.place(x=250, y=364)
                plate_lince = plate_lince.replace('·', ' ')
                # 检测车辆状态
                self.check_car(plate_lince)
                #TODO
                # 更新车位数
                self.check_plackSpace()
            else:
                messagebox.showerror('警告', '请拍摄车牌')

        # 按钮部分
        btn_frame = tk.Frame(self.main_form, width=300, height=200)
        btn_frame.place(x=550, y=560)
        btn1 = tk.Button(btn_frame, text='车牌抓取', width=10, height=4, bg='#dadada', command=self.took_picture)
        btn1.place(x=10, y=60)
        btn2 = tk.Button(btn_frame, text='视频抓取', width=10, height=4, bg='#dadada')
        btn2.place(x=110, y=60)
        btn3 = tk.Button(btn_frame, text='开始检测', width=10, height=4, bg='#dadada', command=check)
        btn3.place(x=220, y=60)
        
        self.main_form.mainloop()

ui = UI()
