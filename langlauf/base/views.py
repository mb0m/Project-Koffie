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
def page1(request):
    return render(request, "base/page1.html")


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
