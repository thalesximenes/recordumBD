from django.contrib import admin
from .models import Disciplinas, Aulas, EixosTematico, MapasTexto

admin.site.register(Aulas)
admin.site.register(Disciplinas)
admin.site.register(EixosTematico)
admin.site.register(MapasTexto)