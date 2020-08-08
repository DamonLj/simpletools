# -*-coding:utf-8-*-

'''删除文件夹下包括所有子目录的bak，dwl，tmp文件'''

__author__ = 'DamonLj'

import os

#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb


class MnsUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)  #初始化此框架的主窗口类
        self.master = master
        self.pack()  #放置框架在窗口上
        self.create_widgets()
        self.master.title("清理文件夹工具")
        self.master.update()  #更新获取窗口大小，用于窗口居中
        # 获取屏幕分辨率，算出窗口左上角坐标定位
        self.x_ = self.master.winfo_screenwidth() / 2 - self.master.winfo_width() / 2
        self.y_ = self.master.winfo_screenheight() / 2 - self.master.winfo_height() / 2
        self.master.geometry("+%d+%d" % (self.x_, self.y_))

    def create_widgets(self):
        l_1 = tk.Label(self, text="文件夹路径:", font=("微软雅黑", 12))
        l_1.grid(row=1, column=0, padx=20)

        self.dirpath = tk.StringVar()
        e_dirpath = tk.Entry(self, textvariable=self.dirpath, font=("微软雅黑", 12))
        e_dirpath.grid(row=1, column=1, ipadx=150)

        b_getdir = tk.Button(self, text="选择文件夹", command=self.get_dirpath, font=("微软雅黑", 12))
        b_getdir.grid(row=1, column=2, padx=20)

        b_makenamesame = tk.Button(self, text="一键清理文件夹", command=self.del_allbak, font=("微软雅黑", 12))
        b_makenamesame.grid(row=2, column=1, pady=20)

        l_explanation = tk.Label(self)
        l_explanation["text"] ='''
*********************************************说  明**********************************************************
                        此程序一键删除文件夹内的所有.bak和.dwl文件，包括子文件夹。
********************************by damon************************ljmgps**********************************
        '''
        l_explanation["justify"] = tk.LEFT  #设置文字左对齐
        l_explanation['font'] = ('微软雅黑', 12)
        l_explanation.grid(row=0, column=1)

    def get_dirpath(self):
        self.path_ = fd.askdirectory()
        self.dirpath.set(self.path_)

    def del_allbak(self):
        d = self.dirpath.get()
        if os.path.exists(d):
            bak_nums = 0
            dwl_nums = 0
            tmp_nums = 0
            for root, dirs, files in os.walk(d):
                for f in files:
                    if f.split('.')[-1] == 'bak':
                        os.remove(os.path.join(root, f))
                        bak_nums += 1
                    elif f.split('.')[-1] == 'dwl' or f.split('.')[-1] == 'dwl2':
                        os.remove(os.path.join(root, f))
                        dwl_nums += 1
                    elif f.split('.')[-1] == 'tmp' or f.split('.')[-1] == 'fas':
                        os.remove(os.path.join(root, f))
                        tmp_nums += 1
            r_message = '删除了%d个bak文件，%d个dwl文件，%d个tmp文件' % (bak_nums, dwl_nums, tmp_nums)
            mb.showinfo(title="Info", message=r_message)  #使用message类弹出新窗口
            self.dirpath.set("")
        else:
            mb.showerror(title="Info", message="文件夹路径错误！")

    def cancel(self):
        self.master.destroy()  #关闭窗口，不是框架，所以是master


root = tk.Tk()
app = MnsUI(master=root)
app.mainloop()
