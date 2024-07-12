from django.contrib import admin
from django.urls import path, include   # ←, includeを追加

urlpatterns = [
    path('cms/', include('cms.urls')),   # ←ここを追加
    path('admin/', admin.site.urls),
]