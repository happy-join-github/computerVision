V2.0

相较于V1.0我们的改进点有

- V1.0使用tkinter进行开发，V2.0我们使用QT进行页面开发
- 分离不同的页面为不同的文件，没有把文件都写在一个文件内，容易修改。
- 抽离了数据库连接的部分，将数据库的配置放在了share.py中进行配置

项目缺点

- 在mainUI.py中我们还是有大量的代码耦合度过高，维护性不好，可扩展性不好。
- 功能过于简单，界面过于简单。
- 数据库设计有待完善

v2.0使用方法

本地需要搭建数据库数据库名为work，里面有两张表，分别为carer和manage。

数据库执行语句

```sql
CREATE DATABASE work;
USE work;
CREATE TABLE carer (
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

数据库的用户名和密码可以在share.py进行配置

需要配置的是user和password。

需要在终端中输入

```bash
cd /homeWorkV2.0.0
pip install -r requirment.txt
cd /homeWorkV2.0.0/code/GUI
python UI.py
```

