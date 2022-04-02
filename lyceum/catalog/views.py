from django.shortcuts import render


def item_list(request):
    context = {}
    return render(request, "catalog/item_list.html", context=context)


def item_detail(request):
    context = {}
    return render(request, "catalog/item_detail.html", context=context)
