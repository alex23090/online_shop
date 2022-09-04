from .models import Item
from django.core.paginator import Paginator


def paginateItems(request, items, number):
    p = Paginator(items, number)
    page = request.GET.get('page')
    items = p.get_page(page)
    return items
