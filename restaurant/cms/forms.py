from django.forms import ModelForm
from cms.models import Restaurant, Review


class RestaurantForm(ModelForm):
    """飲食店のフォーム"""
    class Meta:
        model = Restaurant
        fields = ('name', 'genre', 'seat_count', )


class ReviewForm(ModelForm):
    """レビューのフォーム"""

    class Meta:
        model = Review
        fields = ('comment', 'rating',)
