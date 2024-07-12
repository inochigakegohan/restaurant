from django.shortcuts import render
from django.http import HttpResponse


def restaurant_list(request):
    """飲食店の一覧"""
    return HttpResponse('飲食店の一覧')


def restaurant_edit(request, restaurant_id=None):
    """飲食店の編集"""
    return HttpResponse('飲食店の編集')


def restaurant_del(request, restaurant_id):
    """飲食店の削除"""
    return HttpResponse('飲食店の削除')
