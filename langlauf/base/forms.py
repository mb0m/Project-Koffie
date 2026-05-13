from django import forms
from .models import Profile, Koffieboon, Tasting


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'date_of_birth', 'favorite_method']
        labels = {
            'city': 'Woonplaats',
            'date_of_birth': 'Geboortedatum',
            'favorite_method': 'Favoriete zetmethode',
        }
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class KoffieboonForm(forms.ModelForm):
    class Meta:
        model = Koffieboon
        fields = ['name', 'country_of_origin', 'harvest_season']
        labels = {
            'name': 'Naam van de boon',
            'country_of_origin': 'Land van herkomst',
            'harvest_season': 'Oogstseizoen (bijv. 2023)',
        }


class TastingForm(forms.ModelForm):
    class Meta:
        model = Tasting
        fields = ['bean', 'date', 'description']
        labels = {
            'bean': 'Koffieboon',
            'date': 'Datum',
            'description': 'Smaakomschrijving',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Bijvoorbeeld lekker, cacaoa achtig'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bean'].queryset = Koffieboon.objects.filter(approved=True)
