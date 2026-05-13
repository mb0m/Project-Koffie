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
    path("profiel/<str:username>/", views.publiek_profiel, name="publiek_profiel"),
    path("admin-bonen/", views.admin_bonen, name="admin_bonen"),
    path("eigen-beheer/", views.eigen_beheer, name="eigen_beheer"),
    path("eigen-beheer/bewerk/<int:pk>/", views.tasting_bewerken, name="tasting_bewerken"),
    path("eigen-beheer/verwijder/<int:pk>/", views.tasting_verwijderen, name="tasting_verwijderen"),
    path("register/", views.register, name="register"),
]
