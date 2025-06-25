from django.db import models
from django.contrib.auth.models import AbstractUser

# Perfil de usuário personalizado (herdando de AbstractUser)
class Usuario(AbstractUser):
    PERFIS = (
        ('solicitante', 'Solicitante'),
        ('atendente', 'Atendente'),
        ('admin', 'Administrador'),
    )
    perfil = models.CharField(max_length=20, choices=PERFIS, default='solicitante')
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Chamado(models.Model):
    STATUS = (
        ('aberto', 'Aberto'),
        ('em_andamento', 'Em Andamento'),
        ('resolvido', 'Resolvido'),
        ('fechado', 'Fechado'),
    )

    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='chamados_criados')
    responsavel = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='chamados_atendidos')
    status = models.CharField(max_length=20, choices=STATUS, default='aberto')
    data_abertura = models.DateTimeField(auto_now_add=True)
    data_encerramento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.titulo}"


class Interacao(models.Model):
    TIPOS = (
        ('mensagem', 'Mensagem'),
        ('alteracao_status', 'Alteração de Status'),
        ('comentario', 'Comentário'),
    )

    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, related_name='interacoes')
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS, default='mensagem')
    data_interacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interação #{self.id} no chamado {self.chamado.id}"


class Anexo(models.Model):
    chamado = models.ForeignKey(Chamado, on_delete=models.CASCADE, related_name='anexos')
    interacao = models.ForeignKey(Interacao, on_delete=models.SET_NULL, null=True, blank=True, related_name='anexos')
    nome_arquivo = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='anexos/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_arquivo
