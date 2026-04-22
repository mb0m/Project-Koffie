from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", include('django.contrib.auth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path("newsfeed/", views.newsfeed, name="newsfeed"),
    path("boon-toevoegen/", views.boon_toevoegen, name="boon_toevoegen"),
    path("mijn-tastings/", views.mijn_tastings, name="mijn_tastings"),
    path("profiel/", views.profiel, name="profiel"),
    path("register/", views.register, name="register"),
]
