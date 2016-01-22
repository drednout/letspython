from datetime import datetime

from django.shortcuts import render
from models import Player


def test1(request):
    template_data = {
        "first_name": "Django",
        "last_name": "Unchained",
        "version": "1.0",
        "created": datetime.now()
    }

    return render(request, 'test1.html', template_data)


def test2(request):
    template_data = {
        "player_list": Player.objects.all(),
        "version": "1.0"
    }
    return render(request, 'test2.html', template_data)
