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
        # frame_left.place(relx=0, rely=0, relwidth=1)
        frame_left.pack(side=TOP,fill=X)

        frame_left.grid_columnconfigure(0,weight=2)
        frame_left.grid_rowconfigure(0,weight=1)
        # frame_left.grid_columnconfigure(1, weight=1)
        frame_left.grid_rowconfigure(1, weight=1)
        frame_left.grid_columnconfigure(2, weight=2)
        frame_left.grid_rowconfigure(2, weight=1)
        # frame_left.grid_columnconfigure(3, weight=1)
        frame_left.grid_rowconfigure(3, weight=1)
        self.frame_left2 = LabelFrame(self, text="内容")
        # 使用 place 控制 LabelFrame 的位置
        # frame_left2.place(relx=0, rely=0, relwidth=1)
        self.frame_left2.pack(side=TOP, fill=BOTH)


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
        '''内容'''
        # 内容
        self.treev_con = Treeview(self.frame_left2,columns=("dir","file_name","sql_con"),show='headings',height=2)

        self.treev_con.heading("dir", text="地址")  # 图标栏
        self.treev_con.heading("file_name", text="文件名")
        self.treev_con.heading("sql_con", text="sql数量")

        self.treev_con.column("dir",anchor=CENTER)
        self.treev_con.column("file_name", anchor=CENTER)
        self.treev_con.column("sql_con", anchor=CENTER)

        self.treev_con.tag_configure("evenColor", background="lightblue")  # 设置标签
        self.treev_con.pack(fill=BOTH)




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
            data = self._dir_or_file(v_ipt_dml)
            # data = {"文件名":ls_dir_dml[1],"路径":ls_dir_dml[0]}
            # print(ls_dir_dml[1])
            # # print(type(len(data)))
            rowCount = 1
            for i_data in range(len(data)):
                if (rowCount % 2 == 1):
                    self.treev_con.insert("", index=END, text="文件名", values=(data[i_data]))
                    # print((ls_dir_dml[1])[i_data])
                else:
                    self.treev_con.insert("", index=END, text="文件名", values=(data[i_data]),tags=("evenColor"))  # 建立浅蓝色底
                    # print((ls_dir_dml[1])[i_data])
                rowCount += 1  # 行号数加1

            self.treev_con.pack(fill=BOTH)

        else:
            # message = "输入有误,这不是文件夹"
            tk.messagebox.askokcancel("提示", " 输入有误,这不是文件夹! ")
            # self.but_reset()


    def  _dir_or_file(self,fpath):
        """判断参数是文件还是路径，路径的话遍历路径经将文件路径记录到列表"""
        file_sql_info_ls = []
        for dirpath, dirnames, filenames in os.walk(fpath):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                # file_paths.append(file_path)
                # file_name_ls.append(filename)
                list_tmp = []
                sql_list = self.readsql_from_file(self, file_path, filename)
                list_tmp.append(filename)
                list_tmp.append(file_path)
                list_tmp.append(str(len(sql_list)))
                file_sql_info_ls.append(list_tmp)
        return file_sql_info_ls

    def readsql_from_file(self, file_path, filename):
        try:
            print("sql文件%s，开始内容转化" % (file_path))
            fp = open(file_path, 'r', encoding='utf-8')
            sql_str = fp.readlines()
            # results_list = sql_str.split(";")
            results, results_list = [], []
            ##去除\n\r
            if sql_str[-1].endswith(";"):
                sql_str[-1] = sql_str[-1] + "\n"
            for sql in sql_str:
                if sql.startswith("\n") or sql == "\r":
                    continue
                if sql.startswith("--"):
                    continue
                if not sql.startswith("--") and not sql.endswith("--"):
                    if not sql.startswith("/*"):
                        results.append(sql)

            trmp_res_sql_list, res_sql_list = [], []
            while len(results) > 0:
                for i in range(len(results)):
                    if results[i].endswith(";\n"):
                        tem_str = "".join(results[:i + 1])
                        trmp_res_sql_list.append(tem_str)
                        del results[:i + 1]
                        break
            for i in trmp_res_sql_list:
                if i.endswith(";\n"):
                    i = i.strip()
                    i = i[::-1].replace(";", "", 1)[::-1]
                    res_sql_list.append(i)
            print("sql文件%s，内容转化成功，转化待执行sql共%s条" % (file_path, str(len(res_sql_list))))
            return res_sql_list
        except Exception as ex:
            print("ERROR,sql文件%s，内容转化失败，失败信息%s" % (file_path, str(ex)))
            return None






if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
