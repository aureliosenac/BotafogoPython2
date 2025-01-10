from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('cadastro-produto/', views.cadastro_produto, name='cadastro_produto'),
    path('listar-produtos/', views.listar_produtos, name='listar_produtos'),
]