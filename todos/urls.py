from django.urls import path
from todos.views import (
    TodoList_view,
    TodoList_Details,
    TodoList_Create,
    TodoList_Update,
    TodoList_Delete,
    TodoList_CreateItem,
)

urlpatterns = [
    path("items/create/", TodoList_CreateItem, name="todo_list_item"),
    path("<int:id>/delete/", TodoList_Delete, name="todo_list_delete"),
    path("<int:id>/edit/", TodoList_Update, name="todo_list_update"),
    path("create/", TodoList_Create, name="todo_list_create"),
    path("<int:id>/", TodoList_Details, name="todo_list_detail"),
    path("", TodoList_view, name="todo_list_list"),
]
