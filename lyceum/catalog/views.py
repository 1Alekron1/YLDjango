from django.shortcuts import render, get_object_or_404
from django.http import Http404
from catalog.models import Item, Category
from rating.models import Rating
from .forms import RatingSelect

from django.db.models import Avg, Count


def item_list(request):
    categories = Category.objects.category_and_item_are_published()
    context = {"categories": categories}
    return render(request, "catalog/item_list.html", context=context)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk, is_published=True)
    if request.method == "POST":
        form = RatingSelect(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            object, created = Rating.objects.get_or_create(user=request.user, item=item)
            object.star = int(cd["rating"])
            object.save()
    rating_dict = Rating.choices
    all_ratings = Rating.objects.filter(item=item, star__in=[1, 2, 3, 4, 5]).aggregate(
        Avg("star"), Count("star")
    )
    if request.user.is_authenticated:
        try:
            user_rating = int(Rating.objects.get(item=item, user=request.user).star)
        except Rating.DoesNotExist:
            user_rating = 0
    else:
        user_rating = 0
    form = RatingSelect()
    context = {
        "item": item,
        "all_ratings": all_ratings,
        "user_rating": user_rating,
        "rating_dict": rating_dict,
        "form": form,
    }
    return render(request, "catalog/item_detail.html", context=context)
