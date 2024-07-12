from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 飲食店
    path('restaurant/', views.restaurant_list, name='restaurant_list'),   # 一覧
    path('restaurant/add/', views.restaurant_edit, name='restaurant_add'),  # 登録
    path('restaurant/mod/<int:restaurant_id>/', views.restaurant_edit, name='restaurant_mod'),  # 修正
    path('restaurant/del/<int:restaurant_id>/', views.restaurant_del, name='restaurant_del'),   # 削除
]