from django.contrib import admin
from .models import Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    @admin.display(description='stanowisko')
    def custom_stanowisko(self, obj):
        return f'{obj.stanowisko} ({obj.stanowisko.id})'

    list_display = ['imie', 'nazwisko', 'custom_stanowisko']
    list_filter = ('stanowisko', 'data_dodania')


class StanowiskoAdmin(admin.ModelAdmin):
        list_filter = ['nazwa']


admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)
