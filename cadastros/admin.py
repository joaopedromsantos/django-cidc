from django.contrib import admin

from cadastros.models import Cidade, Estado, Pais


class EstadoInLine(admin.TabularInline):
    model = Estado


class PaisAdmin(admin.ModelAdmin):

    fields = ('nome',)
    inlines = [
        EstadoInLine
    ]


admin.site.register(Cidade)
admin.site.register(Pais, PaisAdmin)
admin.site.register(Estado)

