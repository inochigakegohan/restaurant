from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Restaurant

def restaurant_list(request):
    """飲食店の一覧"""
    restaurants = Restaurant.objects.all().order_by('id')
    return render(request,
                  'cms/restaurant_list.html',  # 使用するテンプレート
                  {'restaurants': restaurants})  # テンプレートに渡す


def restaurant_edit(request, restaurant_id=None):
    """飲食店の編集"""
    return HttpResponse('飲食店の編集')


def restaurant_del(request, restaurant_id):
    """飲食店の削除"""
    return HttpResponse('飲食店の削除')
