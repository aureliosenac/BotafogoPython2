from django.contrib import admin
from .models import Produto

# Registro do modelo Produto no admin
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao')  # Exibe os campos na lista
    search_fields = ('nome', 'descricao')  # Permite pesquisa por nome e descrição
