from django.contrib import admin
from meuapp.models import Contato, Entry

admin.site.register(Contato)
admin.site.register(Entry)
#@admin.register(Contato)
#class ContatoAdmin(admin.ModelAdmin):
  #  list_display = ('nome', 'telefone', 'endereco')
  #  search_fields = ('nome', 'telefone')