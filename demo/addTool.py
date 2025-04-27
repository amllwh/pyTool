import os
import tkinter as tk
from tkinter import filedialog, messagebox


def add_prefix():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    prefix = entry_prefix.get()
    if not prefix:
        messagebox.showwarning("提示", "请先输入前缀！")
        return

    count = 0
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        if os.path.isfile(old_path):
            new_filename = prefix + filename
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            count += 1

    messagebox.showinfo("完成", f"成功重命名 {count} 个文件！")


# 创建窗口
root = tk.Tk()
root.title("批量加前缀小工具")
root.geometry("400x200")

# 文字标签
label = tk.Label(root, text="输入要加的前缀：", font=("Arial", 14))
label.pack(pady=10)

# 前缀输入框
entry_prefix = tk.Entry(root, font=("Arial", 14))
entry_prefix.pack(pady=10)

# 按钮
btn = tk.Button(root, text="选择文件夹并加前缀", font=("Arial", 14), command=add_prefix)
btn.pack(pady=20)

# 启动界面
root.mainloop()
