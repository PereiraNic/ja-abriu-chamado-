from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chamados.urls')), # ← inclui as rotas do app
    path('accounts/', include('django.contrib.auth.urls')), # ← login/logout
]
