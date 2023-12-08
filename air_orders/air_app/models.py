from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

# 大票号
class Big_ticket(models.Model):
    big_ticket_num = models.CharField('大票号', max_length=64, null=True, unique=True)
    big_ticket_status = models.CharField('HBL状态', max_length=2, null=True)
    crate_date = models.DateField('创建日期', auto_now_add=True)
    big_ticket_creator = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    hbl_remake = models.CharField('备注', max_length=200, null=True)
    class Meta:
        managed = True

    def __str__(self):
        return "大票号：%s\tHBL状态：%s\t创建日期：%s\t创建人：%s\t备注：%s" %(self.big_ticket_num,self.big_ticket_status,self.crate_date,self.big_ticket_creator,self.hbl_remake)



# HBL
class Air_orders(models.Model):
    # id = models.AutoField('小票id', primary_key=True)
    hbl_num = models.CharField('HBL号', max_length=64,db_index=True, null=True) #db_index=True添加索引
    big_ticket = models.ForeignKey(Big_ticket, on_delete=models.CASCADE,blank=True, null=True)
    hbl_status = models.CharField('HBL状态', max_length=2)
    create_date = models.DateField('创建日期', auto_now_add=True)
    hbl_creator = models.ForeignKey(User, on_delete=models.DO_NOTHING,blank=True, null=True)
    hbl_remake = models.CharField('备注', max_length=200, null=True)
    class Meta:
        managed = True
        db_table = "air_app_air_orders"

    def __str__(self):
        return "HBL号：%s\t大票ID：%s\t状态：%s\t创建时间：%s\t备注：%s" %(self.hbl_num,self.big_ticket,self.hbl_status,self.create_date,self.hbl_remake)

# 物流轨迹
class Air_track(models.Model):
    # id = models.AutoField('小票id', primary_key=True)
    hbl = models.ForeignKey(Air_orders, on_delete=models.CASCADE,blank=True, null=True)
    track_status = models.CharField('HBL状态', max_length=2)
    happen_date = models.DateField('发生日期', default=datetime.now)
    update_date = models.DateField('最后更新日期', auto_now=True)
    updater = models.ForeignKey(User, on_delete=models.DO_NOTHING,blank=True, null=True)
    track_remake = models.CharField('备注', max_length=200, null=True)
    status_display = models.IntegerField('是否显示', default=0)




# # 用户的类
# class LmsUser(models.Model):
#     id = models.AutoField('id', primary_key=True)
#     username = models.CharField('用户名', max_length=32, unique=True) #unique=True 值唯一
#     password = models.CharField('密码', max_length=32, null=True)
#     user_status = models.IntegerField('用户状态',