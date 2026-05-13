from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from .models import Profile, Tasting, Koffieboon
from .forms import ProfileForm, KoffieboonForm, TastingForm
# Create your views here.


@login_required
def index(request):
    return render(request, "base/index.html")


@login_required
def menu(request):
    return render(request, "base/menu.html")


@login_required
def newsfeed(request):
    tastings = Tasting.objects.order_by('-date')
    return render(request, "base/newsfeed.html", {'tastings': tastings})


@login_required
def boon_toevoegen(request):
    boon_form = KoffieboonForm()

    if request.method == 'POST':
        boon_form = KoffieboonForm(request.POST)
        if boon_form.is_valid():
            boon = boon_form.save(commit=False)
            boon.save()
            messages.success(request, 'Boon ingediend! Een admin keurt deze goed.')
            return redirect('boon_toevoegen')

    return render(request, 'base/boon_toevoegen.html', {'boon_form': boon_form})


@login_required
def mijn_tastings(request):
    tasting_form = TastingForm()

    if request.method == 'POST':
        tasting_form = TastingForm(request.POST)
        if tasting_form.is_valid():
            bean = tasting_form.cleaned_data['bean']
            date = tasting_form.cleaned_data['date']
            if Tasting.objects.filter(user=request.user, bean=bean, date=date).exists():
                messages.error(request, 'Je hebt deze boon op deze dag al geproefd!')
            else:
                tasting = tasting_form.save(commit=False)
                tasting.user = request.user
                tasting.save()
                messages.success(request, 'Tasting opgeslagen!')
                return redirect('mijn_tastings')

    return render(request, "base/mijn_tastings.html", {'tasting_form': tasting_form})


@login_required
def eigen_beheer(request):
    tastings = Tasting.objects.filter(user=request.user).order_by('-date')
    return render(request, 'base/eigen_beheer.html', {'tastings': tastings})


@login_required
def tasting_bewerken(request, pk):
    tasting = get_object_or_404(Tasting, id=pk, user=request.user)
    form = TastingForm(request.POST or None, instance=tasting)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tasting bijgewerkt!')
        return redirect('eigen_beheer')
    return render(request, 'base/tasting_bewerken.html', {'form': form, 'tasting': tasting})


@login_required
def tasting_verwijderen(request, pk):
    tasting = get_object_or_404(Tasting, id=pk, user=request.user)
    if request.method == 'POST':
        tasting.delete()
        messages.success(request, 'Tasting verwijderd.')
        return redirect('eigen_beheer')
    return render(request, 'base/tasting_verwijderen.html', {'tasting': tasting})


@login_required
def profiel(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profiel bijgewerkt!')
            return redirect('profiel')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'base/profiel.html', {'form': form, 'profile': profile})


@login_required
def publiek_profiel(request, username):
    profiel_user = get_object_or_404(User, username=username)
    tastings = Tasting.objects.filter(user=profiel_user).order_by('-date')
    return render(request, 'base/publiek_profiel.html', {
        'profiel_user': profiel_user,
        'tastings': tastings,
    })


@staff_member_required
def admin_bonen(request):
    pending_bonen = Koffieboon.objects.filter(approved=False)
    boon_form = KoffieboonForm()

    if request.method == 'POST':
        if request.POST.get('form_type') == 'goedkeuren':
            boon = get_object_or_404(Koffieboon, id=request.POST.get('boon_id'))
            boon.approved = True
            boon.approved_by = request.user
            boon.save()
            messages.success(request, f'"{boon.name}" is goedgekeurd!')
            return redirect('admin_bonen')

        elif request.POST.get('form_type') == 'afkeuren':
            boon = get_object_or_404(Koffieboon, id=request.POST.get('boon_id'))
            boon.delete()
            return redirect('admin_bonen')

        elif request.POST.get('form_type') == 'nieuwe_boon':
            boon_form = KoffieboonForm(request.POST)
            if boon_form.is_valid():
                boon = boon_form.save(commit=False)
                boon.approved = True
                boon.approved_by = request.user
                boon.save()
                messages.success(request, f'"{boon.name}" is toegevoegd en direct goedgekeurd!')
                return redirect('admin_bonen')

    return render(request, 'base/admin_bonen.html', {
        'pending_bonen': pending_bonen,
        'boon_form': boon_form,
    })


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
