from django.shortcuts import render
from random import sample

from catalog.models import Item


def home(request):
    ids = list(Item.objects.filter(is_published=True).values_list("id", flat=True))
    print(ids)
    if len(ids) >= 3:
        ids = sample(ids, 3)
    items = (
        Item.objects.filter(pk__in=ids).prefetch_related("tags").only("name", "text")
    )
    context = {"items": items}
    return render(request, "homepage/home.html", context=context)
