import pymysql

class SI:
    mainWin = None
    loginWin = None
    registerWin = None

    # 连接数据库
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='000000',
        database='work',
        charset='utf8mb4'
    )
