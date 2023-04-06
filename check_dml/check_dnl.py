"""
Autho:SGL
Version:1.0
QQ交流群:790655549
"""
import os
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

class WinGUI(Tk):

    def __init__(self):
        super().__init__()
        self.title("DML检查")
        self.geometry("800x500")

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
        self.frame_left2.pack(side=TOP, fill=BOTH,expand = True)


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

        '''内容'''
        # 内容
        self.treev_con = Treeview(self.frame_left2,columns=("dir","file_name","sql_con","diff_sql_count"),show='headings',height=2)

        # 滚动条
        yscrollbar = Scrollbar(self.frame_left2)
        yscrollbar.pack(side=RIGHT, fill=Y)
        # tree.configure(yscrollcommand=yscrollbar.set)
        yscrollbar.config(command=self.treev_con.yview)
        self.treev_con.configure(yscrollcommand=yscrollbar.set)  # 经过试验，以上两行代码交换顺序后无影响

        self.treev_con.heading("file_name", text="文件名")
        self.treev_con.heading("dir", text="地址")  # 图标栏
        self.treev_con.heading("sql_con", text="sql数量")
        self.treev_con.heading("diff_sql_count", text="差异数")

        self.treev_con.column("file_name", anchor=W)
        self.treev_con.column("dir",anchor=W)
        self.treev_con.column("sql_con", anchor=W)
        self.treev_con.column("diff_sql_count", anchor=W)

        self.treev_con.pack(fill=BOTH,expand = True)

        """按钮组"""
        # self.tk_button_but_open = self.__tk_button_but_open(frame_left)
        btn_check = Button(frame_left, text="检测",command=self.check_but)
        btn_check.grid(column=0, row=2, padx=(5, 5), pady=(10, 10), ipady=8)

        # self.tk_button_but_cle = self.__tk_button_but_cle(frame_left)
        btn_reset = Button(frame_left, text="重置",command=self.but_reset)
        btn_reset.grid(column=2, row=2, padx=(5, 5), pady=(10, 10), ipady=8)



        btn_look = Button(self.frame_left2, text="查看")
        btn_look.pack(side=BOTTOM,fill=NONE)




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
        for child in self.treev_con.get_children():
            self.treev_con.delete(child)
            self.treev_con.pack(fill=BOTH, expand=True)

    def check_but(self):
        for child in self.treev_con.get_children():
            self.treev_con.delete(child)
            self.treev_con.pack(fill=BOTH, expand=True)
        v_ipt_log = self.ipt_logs.get()
        v_ipt_dml = self.ipt_dml.get()
        logs_all_ls = []
        data =[]
        if os.path.isdir(v_ipt_log) and os.path.isdir(v_ipt_dml):
            # log日志数据提取
            log_file_paths = self._dir_or_file(v_ipt_log)
            for log_file_path in log_file_paths:
                log_sql_lists = self.readsql_from_file(log_file_path)
                for log_sql_list in log_sql_lists:
                    logs_all_ls.append(log_sql_list)
        else:
            tk.messagebox.askokcancel("提示", " log路径输入有误,这不是文件夹! ")

        if os.path.isdir(v_ipt_dml):
            dml_file_paths = self._dir_or_file(v_ipt_dml)
            for file_path in dml_file_paths:
                sql_list = self.readsql_from_file(file_path)
                list_tmp = []
                list_tmp.append(os.path.basename(file_path)) # 文件名
                list_tmp.append(file_path)
                list_tmp.append(len(sql_list))
                # list_tmp.append(str(len(sql_list)))
                count=0
                for dml_sql in sql_list:
                    if dml_sql not in logs_all_ls:
                        count += 1
                        print(dml_sql)
                list_tmp.append(count)
                data.append(list_tmp)


            for i_data in range(len(data)):
                self.treev_con.insert("", index=END, text="文件名", values=(data[i_data]))

            self.treev_con.pack(fill=BOTH)
        else:
            # message = "输入有误,这不是文件夹"
            tk.messagebox.askokcancel("提示", " DML路径输入有误,这不是文件夹! ")
            # self.but_reset()


    def  _dir_or_file(self,fpath):
        """判断参数是文件还是路径，路径的话遍历路径经将文件路径记录到列表"""
        file_paths = []
        for dirpath, dirnames, filenames in os.walk(fpath):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                file_paths.append(file_path)
                # file_name_ls.append(filename)


        return file_paths

    def readsql_from_file(self,file_path):
        try:
            print("sql文件%s，开始内容转化" % (file_path))
            fp = open(file_path, 'r', encoding='UTF-8-sig')
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
            # print("sql文件%s，内容转化成功，转化待执行sql共%s条" % (file_path, str(len(res_sql_list))))
            # print(res_sql_list)
            return res_sql_list
        except Exception as ex:
            print("ERROR,sql文件%s，内容转化失败，失败信息%s" % (file_path, str(ex)))
            tk.messagebox.askokcancel("提示", " DML路径输入有误,这不是文件夹! ")
            return None


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
