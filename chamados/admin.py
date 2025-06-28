from django.contrib import admin
from .models import Usuario, Categoria, Chamado, Interacao, Anexo

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'perfil', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('perfil', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'status', 'categoria', 'solicitante', 'responsavel', 'data_abertura', 'data_encerramento')
    list_filter = ('status', 'categoria', 'data_abertura')
    search_fields = ('titulo', 'descricao')

@admin.register(Interacao)
class InteracaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'chamado', 'autor', 'tipo', 'data_interacao')
    list_filter = ('tipo', 'data_interacao')
    search_fields = ('mensagem',)

@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_arquivo', 'chamado', 'interacao', 'data_upload')
    list_filter = ('data_upload',)

