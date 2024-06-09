V1.0使用方法

本地需要搭建数据库数据库名为homework，里面有两张表，分别为history_user和manage。

数据库执行语句

```sql
CREATE DATABASE homework;
USE homework;
CREATE TABLE history_user (
    plateLince VARCHAR(20) NOT NULL,
    startTime DATETIME NOT NULL,
    endTime DATETIME NOT NULL,
    money INT NOT NULL,
    state INT NOT NULL,
    PRIMARY KEY (plateLince)
);
CREATE TABLE manage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL
);
insert into manage values(1,root,123456)
```

数据库用户为root密码为000000

这样才能连接数据库，修改密码步骤

登录下面指令敲击回车然后输入密码

```bash
mysql -u root -p
```

输入一下命令

```bash
USE mysql;
UPDATE user SET authentication_string=PASSWORD('新密码') WHERE User='root';
FLUSH PRIVILEGES;
关闭数据库并重启mysql服务或者重启电脑
```

需要在终端输入

```
cd /homework/
pip install -r requirement.txt
cd homeWorkV1.0.0/code/GUI/
python UI.py
```

初始用户名root和密码123456
演示效果可以看V1.0.0Docfile里面的ppt或者技术文档
