from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListView, name = "ListView"),
    path('addListItem/', views.addListItem, name="addListItem"),
    path('delete/<int:list_id>/', views.deleteList, name="deleteList"),
    path('addNewList/', views.addNewList, name="addNewList"),
    path('deleteItem/<int:list_item_id>/', views.deleteListItem, name="deleteListItem"),
]