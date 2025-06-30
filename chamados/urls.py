from django.urls import path
from .views import signup_view, painel_usuario_view, novo_chamado, home_view

urlpatterns = [
    path('', home_view, name='home'),  # ← Página inicial
    path('signup/', signup_view, name='signup'),
    path('painel/', painel_usuario_view, name='painel_usuario'),
    path('novo_chamado/', novo_chamado, name='novo_chamado'),
]
