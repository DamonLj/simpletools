#!/user/bin/env python
# -*- coding: utf-8 -*-

'''删除文件夹下包括所有子目录的bak，dwl，tmp文件'''

__author__ = 'DamonLj'

import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb

from mk_proj_dir.mk_proj_dir import Tree

class MnsUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)  #初始化此框架的主窗口类
        self.master = master
        self.pack()  #放置框架在窗口上
        self.create_widgets()
        self.master.title("文件夹目录生成")
        self.master.update()  #更新获取窗口大小，用于窗口居中
        # 获取屏幕分辨率，算出窗口左上角坐标定位
        self.x_ = self.master.winfo_screenwidth() / 2 - self.master.winfo_width() / 2
        self.y_ = self.master.winfo_screenheight() / 3 - self.master.winfo_height() / 2
        self.master.geometry("+%d+%d" % (self.x_, self.y_))

    def create_widgets(self):
        l_explanation = tk.Label(self)
        l_explanation["text"] ='此程序根据tree文件，一键生成项目文件夹结构。'
        l_explanation["justify"] = tk.CENTER  #设置文字左对齐
        l_explanation['font'] = ('微软雅黑', 12)
        l_explanation.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.path_tree = tk.StringVar()
        l_treepath = tk.Label(self, textvariable=self.path_tree, font=("微软雅黑", 12))
        l_treepath.grid(row=1, column=1, ipadx=20, columnspan=2)
        b_gettree = tk.Button(self, text="选择目录结构文件：", command=self.get_filepath, font=("微软雅黑", 12))
        b_gettree.grid(row=1, column=0, padx=20)

        self.path_root = tk.StringVar()
        l_dirpath = tk.Label(self, textvariable=self.path_root, font=("微软雅黑", 12))
        l_dirpath.grid(row=2, column=1, ipadx=20, columnspan=2)
        b_getdir = tk.Button(self, text="选择生成位置：", command=self.get_dirpath, font=("微软雅黑", 12))
        b_getdir.grid(row=2, column=0, padx=20)

        b_makenamesame = tk.Button(self, text="一键生成项目文件夹", command=self.mk_proj_dir, font=("微软雅黑", 12))
        b_makenamesame.grid(row=3, column=0, columnspan=3, pady=20)

        self.tree = tk.StringVar()
        l_treestr = tk.Label(self, textvariable=self.tree,  font=("微软雅黑", 12), justify=tk.LEFT)
        l_treestr.grid(row=4, column=0, columnspan=3)

    def get_filepath(self):
        file_path = fd.askopenfilename(initialdir=os.getcwd())
        self.path_tree.set(file_path)
        if file_path:
            self.read_file()

    def get_dirpath(self):
        dir_path = fd.askdirectory()
        self.path_root.set(dir_path)

    def read_file(self):
        with open(self.path_tree.get(), 'r', encoding='utf-8') as f:
            self.tree.set(f.read())

    def mk_proj_dir(self):
        tree = Tree()
        tree.mk_tree_from_txt(self.path_tree.get())
        tree.mk_dir_from_tree(self.path_root.get())
        if tree.tree:
            mb.showinfo(title="Info", message="创建文件夹成功！")  # 使用message类弹出新窗口
            self.path_root.set("")

    def cancel(self):
        self.master.destroy()  #关闭窗口，不是框架，所以是master


root = tk.Tk()
app = MnsUI(master=root)
app.mainloop()
