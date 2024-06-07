import tkinter as tk
from tkinter import ttk

# 创建主窗口
root = tk.Tk()
root.title("表格示例")

# 创建Treeview
treeview = ttk.Treeview(root, columns=("id", "plateLine", "startTime"), show='headings')
treeview.pack()

# 设置表头
treeview.heading("id", text="ID")
treeview.heading("plateLine", text="车牌号")
treeview.heading("startTime", text="开始时间")

# 设置列宽
treeview.column("id", width=50)
treeview.column("plateLine", width=100)
treeview.column("startTime", width=150)

# 添加数据行
data = [
    ("1", "鲁Qsfc4d", "2024-05-29 11:20:12"),
    ("2", "鲁Qxfb4d", "2024-05-29 11:30:20")
]

for item in data:
    treeview.insert("", tk.END, values=item)

# 启动事件循环
root.mainloop()
