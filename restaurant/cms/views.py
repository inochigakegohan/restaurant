from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from cms.models import Restaurant, Review
from cms.forms import RestaurantForm, ReviewForm
from django.views.generic.list import ListView


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


class ReviewList(ListView):
    """レビューの一覧"""
    context_object_name = 'reviews'
    template_name = 'cms/review_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        restaurant = get_object_or_404(Restaurant, pk=kwargs['restaurant_id'])  # 親の飲食店を読む
        reviews = restaurant.reviews.all().order_by('id')  # 飲食店の子供の、レビューを読む
        self.object_list = reviews

        context = self.get_context_data(object_list=self.object_list, restaurant=restaurant)
        return self.render_to_response(context)


def review_edit(request, restaurant_id, review_id=None):
    """レビューの編集"""
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)  # 親の飲食店を読む
    if review_id:  # review_id が指定されている (修正時)
        review = get_object_or_404(Review, pk=review_id)
    else:  # review_id が指定されていない (追加時)
        review = Review()

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)  # POST された request データからフォームを作成
        if form.is_valid():  # フォームのバリデーション
            review = form.save(commit=False)
            review.restaurant = restaurant  # このレビューの、親の飲食店をセット
            review.save()
            return redirect('cms:review_list', restaurant_id=restaurant_id)
    else:  # GET の時
        form = ReviewForm(instance=review)  # review インスタンスからフォームを作成

    return render(request,
                  'cms/review_edit.html',
                  dict(form=form, restaurant_id=restaurant_id, review_id=review_id))
