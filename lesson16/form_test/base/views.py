from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import models
from . import forms


def player_changed(request, player_id):
    template_data = {
        "player_id": player_id
    }
    return render(request, "player_changed.html", template_data)


def change_player_django_form(request, player_id):
    player = models.Player.objects.get(id=player_id)
    form = forms.PlayerChangeForm(data={"email": player.email, "name": player.name})
    if request.method == 'POST':
        form = forms.PlayerChangeForm(request.POST)
        if form.is_valid():
            player.email = form.cleaned_data["email"]
            player.name = form.cleaned_data["name"]
            player.save()
            return HttpResponseRedirect("/player_changed/%d" % player.id)

    template_data = {
        "form": form,
        "player": player
    }

    return render(request, 'change_player_django.html', template_data)




def change_player(request, player_id):
    player = models.Player.objects.get(id=player_id)
    template_data = {
        "player": player
    }
    if request.method == "POST":
        player.email = request.POST["email"]
        player.name = request.POST["name"]
        player.save()
        return render(request, "player_changed.html", {"player_id": player.id})

    return render(request, "change_player.html", template_data)
