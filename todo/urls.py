from django.urls import path
from . import views

urlpatterns = [
    # Página inicial: lista todas as listas de TO DO
    path('', views.index, name='index'),

    # Criar nova lista de TO DO
    path('lista/nova/', views.create_list, name='create_list'),

    # Detalhes de uma lista (exibe os itens)
    path('lista/<int:list_id>/', views.list_detail, name='list_detail'),

    # Criar um novo item na lista
    path('lista/<int:list_id>/item/nova/', views.create_item, name='create_item'),

    # Editar um item existente
    path('item/<int:item_id>/editar/', views.edit_item, name='edit_item'),

    # Excluir um item
    path('item/<int:item_id>/excluir/', views.delete_item, name='delete_item'),
]
