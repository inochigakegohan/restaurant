from django.forms import ModelForm
from cms.models import Restaurant


class RestaurantForm(ModelForm):
    """飲食店のフォーム"""
    class Meta:
        model = Restaurant
        fields = ('name', 'genre', 'seat_count', )