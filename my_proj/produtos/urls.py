from django.urls import path
from . import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),  # Lista de produtos
    path('view/<int:pk>/', views.produto_view, name='produto_view'),  # Visualizar produto
    path('new/', views.produto_create, name='produto_new'),  # Criar novo produto
    path('detail/<int:pk>/', views.produto_view, name='produto_detail'),  # Detalhes do produto
    path('edit/<int:pk>/', views.produto_update, name='produto_edit'),  # Editar produto
    path('delete/<int:pk>/', views.produto_delete, name='produto_delete'),  # Deletar produto
]
