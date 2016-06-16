from django.db import models
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from lists.models import Item


def new_list(request):
    Item.objects.create(
        text=request.POST.get('item_text'),
    )

    return redirect(reverse('only'))
