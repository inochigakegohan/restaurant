from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    # 飲食店
    path('v1/restaurants/', views.restaurant_list, name='restaurant_list'),   # 一覧
]