from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 飲食店
    path('restaurant/', views.restaurant_list, name='restaurant_list'),  # 一覧
    path('restaurant/add/', views.restaurant_edit, name='restaurant_add'),  # 登録
    path('restaurant/mod/<int:restaurant_id>/', views.restaurant_edit, name='restaurant_mod'),  # 修正
    path('restaurant/del/<int:restaurant_id>/', views.restaurant_del, name='restaurant_del'),  # 削除
    # レビュー
    path('review/<int:restaurant_id>/', views.ReviewList.as_view(), name='review_list'),  # 一覧
    path('review/add/<int:restaurant_id>/', views.review_edit, name='review_add'),  # 登録
    path('review/mod/<int:restaurant_id>/<int:review_id>/', views.review_edit, name='review_mod'),  # 修正
    path('review/del/<int:restaurant_id>/<int:review_id>/', views.review_del, name='review_del'),  # 削除
]
