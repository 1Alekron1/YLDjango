from django.shortcuts import render, get_object_or_404
from django.http import Http404
from catalog.models import Item


def item_list(request):
    items = (
        Item.objects.filter(is_published=True)
        .prefetch_related("tags")
        .only("name", "text")
    )
    context = {"items": items}
    return render(request, "catalog/item_list.html", context=context)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.is_published == True:
        context = {"item": item}
        return render(request, "catalog/item_detail.html", context=context)
    raise Http404("Товар не существует или не опубликован")
