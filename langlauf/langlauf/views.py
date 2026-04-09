# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required
def index(request):
    return render(request, "base/index.html")


def page1(request):
    return render(request, "page1/page1.html")
