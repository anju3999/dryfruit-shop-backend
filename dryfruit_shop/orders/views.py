from django.http import JsonResponse, HttpResponse
from .models import Order

def order_list(request):
    # orders = Order.objects.all().values('id', 'user', 'order_date', 'status', 'total_amount')
    return HttpResponse('Orders list here')

def order_detail(request):
    return HttpResponse('Order detail here')