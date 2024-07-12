from django.contrib import admin
from cms.models import Restaurant, Review


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre', 'seat_count',)  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目


admin.site.register(Restaurant, RestaurantAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('restaurant',)   # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）


admin.site.register(Review, ReviewAdmin)