from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from lists.models import Item


def home(request):

    if request.method == 'POST':
        new_item_text = request.POST.get('item_text')
        Item.objects.create(
            text=new_item_text,
        )
        return redirect(reverse('home'))
    else:
        new_item_text = ''

    items = Item.objects.all()

    return render(
        request,
        "home.html",
        {'items': items},
    )
