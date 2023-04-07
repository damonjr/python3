import os


def readsql_from_file(sqlfile_path):
    try:
        print("sql文件%s，开始内容转化" % (sqlfile_path))
        fp = open(sqlfile_path, 'r', encoding='utf-8')
        sql_str = fp.readlines()
        # results_list = sql_str.split(";")
        results, results_list = [], []
        ##去除\n\r
        if sql_str[-1].endswith(";"):
            sql_str[-1] = sql_str[-1] + "\n"
        for sql in sql_str:
            if sql.startswith( "\n") or sql == "\r":
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
        print("sql文件%s，内容转化成功，转化待执行sql共%s条" % (sqlfile_path, str(len(res_sql_list))))
        return res_sql_list
    except Exception as ex:
        print("ERROR,sql文件%s，内容转化失败，失败信息%s" % (sqlfile_path, str(ex)))
        return None
if __name__ == "__main__":
    # sql_list = readsql_from_file(r'E:/NAS/SynologyDrive/ChinaTelecom/工作记录/03/0316/MBDM1.1.0_1_20230222/程序包/脚本/DML/mbdm_conf\02_MBDM1.1.0_1_20230222_DML_mbdm_conf_钟家铖_增量1_活动结果统计数据入库定时任务_20230221.sql')
    fpath = ('E:/NAS/SynologyDrive/ChinaTelecom/工作记录/03/0316/MBDM1.1.0_1_20230222/程序包/脚本/DML/mbdm_conf')
    for dirpath, dirnames, filenames in os.walk(fpath):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # file_paths.append(file_path)
            # file_name_ls.append(filename)

            sql_list = readsql_from_file(file_path)
        for sql_str in range(len(sql_list)):
            print("第%s条SQL"%(str(sql_str)),sql_list[sql_str])




