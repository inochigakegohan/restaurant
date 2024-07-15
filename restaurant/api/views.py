import json
from collections import OrderedDict
from django.http import HttpResponse
from cms.models import Restaurant


def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response


def restaurant_list(request):
    """飲食店とレビューのJSONを返す"""
    restaurants = []
    for restaurant in Restaurant.objects.all().order_by('id'):

        reviews = []
        for review in restaurant.reviews.order_by('id'):
            review_dict = OrderedDict([
                ('id', review.id),
                ('comment', review.comment),
            ])
            reviews.append(review_dict)

        restaurant_dict = OrderedDict([
            ('id', restaurant.id),
            ('name', restaurant.name),
            ('genre', restaurant.genre),
            ('seat_count', restaurant.seat_count),
            ('reviews', reviews)
        ])
        restaurants.append(restaurant_dict)

    data = OrderedDict([('restaurants', restaurants)])
    return render_json_response(request, data)
