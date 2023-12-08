from django.shortcuts import render
# from air_orders.air_app import models
from air_app.models import Air_orders,Big_ticket,Air_track
from django.http import JsonResponse
import json
# from django.db.models import Q
# Create your views here.


# def orders_list(request):
#     airOrders = Air_orders.objects.all()
#     print("+++++")
#     # print(air_orders)
#     return render(request, 'hbl_list.html', {'hbl_list': airOrders})


def get_hbl(request):
    """获取委托单数据"""
    try:
        obj_hbl = Air_orders.objects.select_related('big_ticket_id').all().values('id','hbl_num','big_ticket__big_ticket_num','hbl_status','create_date','hbl_creator_id','hbl_remake')
        print(obj_hbl)
        # 把结果转换为list
        hbl_list = list(obj_hbl)

        return JsonResponse({'code': 1, 'data': hbl_list})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "获取数据异常:"+str(e)})

def query_hbl(request):
    """查询HBL信息"""
    #接收传递过来的查询条件--axios默认时json --字典类型（'inputstr')--data['inputstr']
    data = json.loads(request.body.decode('utf-8'))
    try:
        #获取满足条件的信息
        obj_hbl = Air_orders.objects.filter(hbl_num__icontains=data['inputstr']).values()
        # 把结果转换为list
        hbl_list = list(obj_hbl)

        return JsonResponse({'code': 1, 'data': hbl_list})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "获取数据异常:"+str(e)})

def is_exsits_hblNum(request):
    """判断HBL是否存在"""
    # 接受前端信息
    data = json.loads(request.body.decode('utf-8'))

    obj_hbls = Air_orders.objects.filter(hbl_num=data['hbl_num'], hbl_status=0)
    try:
        if obj_hbls.count() == 0:
            return JsonResponse({'code': 1, 'exists':False})
        else:
            return JsonResponse({'code': 1, 'exists':True})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg':"校验失败："+str(e)})