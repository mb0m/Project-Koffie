from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path("page1/", views.page1, name="page1"),
    path("register/", views.register, name="register"),
]
