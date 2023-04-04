"""
本代码由[Tkinter布局助手]生成
当前版本:3.1.2
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

class WinGUI(Tk):

    def __init__(self):
        super().__init__()
        self.title("Tkinter布局助手")
        self.geometry("600x500")

        self.select_path_dml = StringVar()
        self.select_path_logs = StringVar()
        # 定义第一个容器，使用 labelanchor ='w' 来设置标题的方位
        frame_left = LabelFrame(self, text="请选择")
        # 使用 place 控制 LabelFrame 的位置
        frame_left.place(relx=0, rely=0, relwidth=1)

        frame_left.grid_columnconfigure(0,weight=2)
        frame_left.grid_rowconfigure(0,weight=1)
        # frame_left.grid_columnconfigure(1, weight=1)
        frame_left.grid_rowconfigure(1, weight=1)
        frame_left.grid_columnconfigure(2, weight=2)
        frame_left.grid_rowconfigure(2, weight=1)
        # frame_left.grid_columnconfigure(3, weight=1)
        frame_left.grid_rowconfigure(3, weight=1)


        '''第一组'''
        # self.tk_label_la_dml = self.__tk_label_la_dml(frame_left)
        # DML提示
        label_dml = Label(frame_left, text="请打开DML文件目录:", anchor="sw")
        label_dml.grid(column=0, row=0, padx=(30, 0), pady=(20, 0), ipady=5, sticky=NSEW)

        # self.tk_input_inp_dml = self.__tk_input_inp_dml(frame_left)
        # DML文本框
        self.ipt_dml = Entry(frame_left , textvariable = self.select_path_dml)
        # ipt.place( y=60, relx=0.2, height=24)
        self.ipt_dml.grid(column=0, row=1, padx=(30, 10), sticky=NSEW)

        # self.tk_button_but_dml = self.__tk_button_but_dml(frame_left)
        # DML按钮
        btn_dml = Button(frame_left, text="打开",command=self.select_folder_dml)
        btn_dml.grid(column=1, row=1, padx=(5, 5), sticky=NSEW)

        '''第二组'''
        # self.tk_label_la_logs = self.__tk_label_la_logs(frame_left)
        # logs提示
        label_logs = Label(frame_left, text="请打开Logs日志文件目录:", anchor="sw")
        label_logs.grid(column=2, row=0, padx=(30, 0), pady=(20, 0), ipady=5, sticky=NSEW)
        # logs输入框
        # self.tk_input_inp_logs = self.__tk_input_inp_logs(frame_left)
        self.ipt_logs = Entry(frame_left , textvariable = self.select_path_logs)
        self.ipt_logs.grid(column=2, row=1, padx=(30, 10), sticky=NSEW)
        # logs按钮
        # self.tk_button_but_logs = self.__tk_button_but_logs(frame_left)
        btn_logs = Button(frame_left, text="打开",command=self.select_folder_logs)
        btn_logs.grid(column=3, row=1, padx=(5, 5), sticky=NSEW)
        """按钮组"""
        # self.tk_button_but_open = self.__tk_button_but_open(frame_left)
        btn_check = Button(frame_left, text="检测",command=self.check_but)
        btn_check.grid(column=0, row=2, padx=(5, 5), pady=(10, 10), ipady=8)

        # self.tk_button_but_cle = self.__tk_button_but_cle(frame_left)
        btn_reset = Button(frame_left, text="重置",command=self.but_reset)
        btn_reset.grid(column=2, row=2, padx=(5, 5), pady=(10, 10), ipady=8)
        '''选项卡'''
        # 选项卡
        self.tk_tabs_tab_main = Frame_tab_main(self)

    def select_folder_dml(self):
        # 文件夹选择
        selected_folder_dml = filedialog.askdirectory()  # 使用askdirectory函数选择文件夹
        self.select_path_dml.set(selected_folder_dml)
    def select_folder_logs(self):
        # 文件夹选择
        selected_folder_logs = filedialog.askdirectory()  # 使用askdirectory函数选择文件夹
        self.select_path_logs.set(selected_folder_logs)
    def but_reset(self):
        self.select_path_dml.set("")
        self.select_path_logs.set("")

    def check_but(self):
        v_ipt_log = self.ipt_logs.get()
        v_ipt_dml = self.ipt_dml.get()
        if os.path.isdir(v_ipt_log) and os.path.isdir(v_ipt_dml):
            ls_dir_dml = self._dir_or_file(v_ipt_dml)
            ls_dir_log = self._dir_or_file(v_ipt_log)
            print(ls_dir_dml,ls_dir_dml)

        else:
            # message = "输入有误,这不是文件夹"
            tk.messagebox.askokcancel("提示", " 输入有误,这不是文件夹! ")
            # self.but_reset()


    def  _dir_or_file(self,fpath):
        """判断参数是文件还是路径，路径的话遍历路径经将文件路径记录到列表"""
        self.file_paths = []
        for dirpath, dirnames, filenames in os.walk(fpath):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                self.file_paths.append(file_path)
        return self.file_paths



class Frame_tab_main(Notebook):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        self.tk_tabs_tab_main_0 = Frame_tab_main_0(self)
        self.add(self.tk_tabs_tab_main_0, text="选项卡1")

        self.tk_tabs_tab_main_1 = Frame_tab_main_1(self)
        self.add(self.tk_tabs_tab_main_1, text="选项卡2")

        # self.place(x=19, y=130, width=561, height=361)
        # self.place(x=19, y=330, width=561, height=361)
        self.pack(side="bottom", fill=BOTH)


class Frame_tab_main_0(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        # self.place(x=19, y=123, width=561, height=361)
        self.pack(side="bottom", fill=BOTH)

class Frame_tab_main_1(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__frame()

    def __frame(self):
        # self.place(x=19, y=123, width=561, height=361)
        self.pack(side="bottom", fill=BOTH)




if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
