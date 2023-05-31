from django.urls import path
from todos.views import TodoList_view, TodoList_Details, TodoList_Create

urlpatterns = [
    path("create/", TodoList_Create, name="todo_list_create"),
    path("<int:id>/", TodoList_Details, name="todo_list_detail"),
    path("", TodoList_view, name="todo_list_list"),
]
