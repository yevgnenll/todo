from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from lists.models import Item


def home(request):

    return render(
        request,
        "home.html",
    )
