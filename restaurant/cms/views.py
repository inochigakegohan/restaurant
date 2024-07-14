from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cms.models import Restaurant
from cms.forms import RestaurantForm


def restaurant_list(request):
    """飲食店の一覧"""
    restaurants = Restaurant.objects.all().order_by('id')
    return render(request,
                  'cms/restaurant_list.html',  # 使用するテンプレート
                  {'restaurants': restaurants})  # テンプレートに渡す


def restaurant_edit(request, restaurant_id=None):
    """飲食店の編集"""
    # return HttpResponse('飲食店の編集')
    if restaurant_id:  # restaurant_id が指定されている (修正時)
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    else:  # restaurant_id が指定されていない (追加時)
        restaurant = Restaurant()

    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            restaurant = form.save(commit=False)
            restaurant.save()
            return redirect('cms:restaurant_list')
    else:  # GET の時
        form = RestaurantForm(instance=restaurant)  # restaurant インスタンスからフォームを作成

    return render(request, 'cms/restaurant_edit.html', dict(form=form, restaurant_id=restaurant_id))


def restaurant_del(request, restaurant_id):
    """飲食店の削除"""
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    restaurant.delete()
    return redirect('cms:restaurant_list')