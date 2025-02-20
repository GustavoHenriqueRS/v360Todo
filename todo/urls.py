from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.user_email_view, name='user_email'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('user_todo_lists/', views.user_todo_lists, name='user_todo_lists'),
    path('lista/nova/', views.create_list, name='create_list'),
    path('lista/<int:list_id>/', views.list_detail, name='list_detail'),
    path('lista/<int:list_id>/excluir/', views.delete_list, name='delete_list'),
    path('lista/<int:list_id>/item/nova/', views.create_item, name='create_item'),
    path('item/<int:item_id>/editar/', views.edit_item, name='edit_item'),
    path('item/<int:item_id>/excluir/', views.delete_item, name='delete_item'),
]
