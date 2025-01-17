from django.db import models


class Restaurant(models.Model):
    """飲食店"""
    name = models.CharField('店名', max_length=255)
    genre = models.CharField('ジャンル', max_length=255, blank=True)
    seat_count = models.IntegerField('席数', blank=True, default=0)

    def __str__(self):
        return self.name


class Review(models.Model):
    """レビュー"""
    restaurant = models.ForeignKey(Restaurant, verbose_name='店名', related_name='reviews', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment

