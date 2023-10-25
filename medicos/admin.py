from django.contrib import admin

from .models import Especialidade, Medico, Agenda, Consulta, Horario, Unidade


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)
    list_filter = ('nome',)
    empty_value_display = '-vazio-'

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'especialidade', 'unidade')
    search_fields = ('nome', 'crm', 'especialidade__nome', 'unidade__nome')
    ordering = ('nome',)
    list_filter = ('nome', 'especialidade__nome', 'unidade__nome')
    empty_value_display = '-vazio-'

class AgendaAdmin(admin.ModelAdmin):
    list_display = ('medico', 'dia', 'horario_inicio', 'horario_fim')
    search_fields = ('medico__nome', 'dia', 'horario_inicio', 'horario_fim')
    ordering = ('dia', 'horario_inicio')
    list_filter = ('dia', 'horario_inicio')
    empty_value_display = '-vazio-'

class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)
    list_filter = ('nome',)
    empty_value_display = '-vazio-'



admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Consulta)
admin.site.register(Horario)
admin.site.register(Unidade, UnidadeAdmin)
