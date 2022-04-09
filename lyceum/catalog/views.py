from django.shortcuts import render, get_object_or_404
from django.http import Http404
from catalog.models import Item, Category


def item_list(request):
    categories = Category.objects.category_and_item_are_published()
    context = {"categories": categories}
    return render(request, "catalog/item_list.html", context=context)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk, is_published=True)
    context = {"item": item}
    return render(request, "catalog/item_detail.html", context=context)
