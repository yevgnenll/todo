from django.shortcuts import render
from lists.models import Item


def view_list(request):

    items = Item.objects.all()

    return render(
        request,
        "lists/list.html",
        {'items': items},
    )
