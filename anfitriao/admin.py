from django.contrib import admin

from anfitriao.models import (Anfitriao, Hospede, Imovel, Reserva, ToDo)


class AnfitriaoAdmin(admin.ModelAdmin):
    fields = ['nome', 'telefone', 'email']


class HospedeAdmin(admin.ModelAdmin):
    fields = ['nome', 'numero_documento', 'telefone', 'email']


class ImovelAdmin(admin.ModelAdmin):
    fields = ['logradoro', 'numero', 'bairro', 'complemento', 'cep', 'cidade', 'uf',
              'valor_diaria', 'quantidade_pessoas', 'pets', 'quantidade_pets']


class ReservaAdmin(admin.ModelAdmin):
    fields = ['imovel', 'hospede', 'data_check_in', 'data_check_out']


class ToDoAdmin(admin.ModelAdmin):
    fields = ['data', 'status', 'anfitriao', 'tarefa', 'reserva', 'imovel']
    list_display = ['data', 'status', 'anfitriao', 'tarefa', 'reserva', 'imovel']


admin.site.register(Anfitriao, AnfitriaoAdmin)
admin.site.register(Hospede, HospedeAdmin)
admin.site.register(Imovel, ImovelAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(ToDo, ToDoAdmin)
