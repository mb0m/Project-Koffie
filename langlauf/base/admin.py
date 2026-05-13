from django.contrib import admin
from .models import Koffieboon, Tasting, Profile


@admin.register(Koffieboon)
class KoffieboonAdmin(admin.ModelAdmin):
    list_display = ['name', 'country_of_origin', 'harvest_season', 'approved', 'approved_by']
    list_editable = ['approved']


admin.site.register(Tasting)
admin.site.register(Profile)
