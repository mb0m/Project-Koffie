# from .models import Distance, Time
from django.shortcuts import render, redirect
from django.http import HttpResponse
# from .forms import NameForm, DistanceForm, TimeForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from django.db.models import Min, Max, Avg
# Create your views here.


@login_required
def index(request):
    return render(request, "base/index.html")


@login_required
def menu(request):
    return render(request, "base/menu.html")


@login_required
def newsfeed(request):
    return render(request, "base/newsfeed.html")


@login_required
def boon_toevoegen(request):
    return render(request, "base/boon_toevoegen.html")


@login_required
def mijn_tastings(request):
    return render(request, "base/mijn_tastings.html")


@login_required
def profiel(request):
    return render(request, "base/profiel.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in and redirect to index
            login(request, user)
            return redirect("index")

    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/register.html", context)
