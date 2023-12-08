const app = new Vue({
    el: '#app',
    data() {
        const rulesHblNum = (rule, value, callback) => {
            // 使用Axios进行校验
            axios.post(
                this.baseURL + 'hbl/check/',
                {
                    hbl_num: value,
                }
            )
                .then((res) => {
                    if (res.data.code === 1) {
                        if (res.data.exists) {
                            callback(new Error("HBL号已存在!"));
                        } else {
                            callback();
                        }
                    } else {
                        //请求失败
                        callback(new Error("后端异常！"))
                    }
                })
                .catch((err) => {
                    //error
                    console.log(err);
                });
        }
        return {
            pickerOptions: {
                shortcuts: [{
                    text: '最近一周',
                    onClick(picker) {
                        const end = new Date();
                        const start = new Date();
                        start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
                        picker.$emit('pick', [start, end]);
                    }
                }, {
                    text: '最近一个月',
                    onClick(picker) {
                        const end = new Date();
                        const start = new Date();
                        start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
                        picker.$emit('pick', [start, end]);
                    }
                }, {
                    text: '最近三个月',
                    onClick(picker) {
                        const end = new Date();
                        const start = new Date();
                        start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
                        picker.$emit('pick', [start, end]);
                    }
                }]
            },
            status_options: [{
                value: '选项1',
                label: '可修改'
            }, {
                value: '选项2',
                label: '已入仓'
            }, {
                value: '选项3',
                label: '机场已收货'
            }, {
                value: '选项4',
                label: '已起飞'
            }, {
                value: '选项5',
                label: '中转中'
            }, {
                value: '选项6',
                label: '到达目的地'
            }, {
                value: '选项7',
                label: '目的地入仓'
            }, {
                value: '选项8',
                label: '派送中'
            }, {
                value: '选项9',
                label: '已签收'
            }],
            tableData: [],
            pageTableData: [],//分页后显示当前页信息
            // 后端请求地址
            baseURL: "http://127.0.0.1:8000/",
            input_hbl: '',//HBL 查询条件
            order_inquiry: {
                input_hbl: '',//HBL 查询条件
                input_status: [],
                date_inquiry: ''
            },

            total: 0, //数据总行数
            currentpage: 1,//当前所在的页面
            pagesize: 10, //每页显示多少行
            //对话框默认不显示
            dialogVisible: false,
            dialogTitle: "",//弹出框标题
            isView: false, //是否为查看
            isEdit: false, //是否是维护
            ordersForm: {
                hbl_num: '',
                big_ticket_num: '',
                hbl_status: '',
                create_date: '',
                hbl_creator: '',
                hbl_remake: '',
                track_domains: [{
                    happen_date: '',
                    track_status: '',
                    track_remake: '',
                    status_display: ''
                }]
            },
            rules: {
                hbl_num: [
                    {required: true, message: "不能为空", trigger: 'blur'},
                    {pattern: /^[A-Za-z0-9_]+$/, message: '只能存在数字、字母、下划线', triggler: 'blur'},
                ],
                // // big_ticket_num: [],
                hbl_status: [
                    {required: true, message: "不能为空", trigger: 'blur'},
                ]
                // create_date: [],
                // hbl_creator: [],
                // hbl_remake: [],
            },
        };

    },

    mounted() {
        this.get_hbl()
    },
    methods: {
        get_hbl: function () {
            // 记录this的地址
            let that = this
            //使用Axios实现Ajax请求
            axios
                .get(this.baseURL + "hbl/")
                .then(function (res) {
                    console.log(res)
                    //请求成功后执行的函数
                    if (res.data.code === 1) {
                        // 把数据给表格
                        that.tableData = res.data.data;
                        //获取返回记录的总行数
                        that.total = res.data.data.length
                        //获取当前页的数据
                        that.getPageTableData()
                        // 提示；
                        that.$message({
                            showClose: true,
                            message: '数据加载成功',
                            type: 'success'
                        });
                    } else {
                        // 失败的提示
                        that.$message.error({
                            showClose: true,
                            message: res.data.msg,
                            type: 'error'
                        });
                    }
                })
                .catch(function (err) {
                    console.log(err)
                })
        },
        //重置
        get_AllOrders() {
            //清空搜索框
            this.input_hbl = ""
            this.get_hbl()

        },
        // 获取当前页的数据
        getPageTableData() {
            // 清空PageTableData的数据
            this.pageTableData = [];
            for (let i = (this.currentpage - 1) * this.pagesize; i < this.total; i++) {
                //遍历数据添加到PageTableData
                this.pageTableData.push(this.tableData[i]);
                //判断是否达到一页的要求
                if (this.pageTableData.length == this.pagesize) break;
            }
        },
        // 查询
        queryOrders() {
            // 使用ajax请求--post-->传递数据
            let that = this
            //开始ajax请求
            axios
                .post(
                    that.baseURL + "hbl/query/",
                    {
                        // inputstr: that.input_hbl
                        inputstr: that.order_inquiry
                    }
                )
                .then(function (res) {
                    if (res.data.code === 1) {
                        that.tableData = res.data.data
                        //获取返回记录的总行数
                        that.total = res.data.data.length
                        //获取当前页的数据
                        that.getPageTableData()
                        // 提示；
                        that.$message({
                            showClose: true,
                            message: '数据加载成功',
                            type: 'success'
                        });
                    } else {
                        // 失败的提示
                        that.$message.error({
                            showClose: true,
                            message: res.data.msg,
                            type: 'error'
                        });

                    }

                })
                .catch(function (err) {
                    console.log(err)
                    that.$message.error("获取数据异常！");
                });
        },
        // 新增数据
        addorder() {
            this.dialogTitle = "新增";
            this.dialogVisible = true;
        },
        //分页时修改每一页的行数
        handleSizeChange(size) {
            //修改当前页行数
            this.pagesize = size;
            // 将数据重新分页
            this.getPageTableData()
        },
        //查看明细
        viewOrder(row) {
            this.dialogTitle = "查看";
            //弹出表单
            this.dialogVisible = "true";
            this.isView = true;
            // console.log(row)
            // 深拷贝复制01
            // this.ordersForm.hbl_num = row.hbl_num;
            // this.ordersForm.big_ticket_num = row.big_ticket_num;
            // this.ordersForm.hbl_status = row.hbl_status;
            // this.ordersForm.create_date = row.create_date;
            // this.ordersForm.hbl_creator = row.hbl_creator;
            // this.ordersForm.hbl_remake = row.hbl_remake;
            //深拷贝复制02
            this.ordersForm = JSON.parse(JSON.stringify(row));

        },
        //维护明细
        updateOrder(row) {
            // 标题修改
            this.dialogTitle = "维护";
            this.isEdit = true;
            //弹出表单
            this.dialogVisible = "true";
            this.ordersForm = JSON.parse(JSON.stringify(row));

        },
        //关闭弹窗并清空表单缓存
        closeDialogForm() {
            //清空
            this.ordersForm.hbl_num = "";
            this.ordersForm.big_ticket_num = "";
            this.ordersForm.hbl_status = "";
            this.ordersForm.create_date = "";
            this.ordersForm.hbl_creator = "";
            this.ordersForm.hbl_remake = "";
            this.ordersForm.track_domains = [];
            this.dialogVisible = false;
            this.isEdit = false;
            this.isView = false;
        },
        addTrackDomain() {
            this.ordersForm.track_domains.push({
                value: '',
                key: Date.now()
            });
        },
        removeTrackDomain(item) {
            var index = this.ordersForm.track_domains.indexOf(item)
            if (index !== -1) {
                this.ordersForm.track_domains.splice(index, 1)
            }
        },
        //调整当前页码
        handleCurrentChange(pageNumber) {
            // 修改当前页的页码
            this.currentpage = pageNumber;
            // 将数据重新分页
            this.getPageTableData();
        }
    },
})