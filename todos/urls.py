from django.urls import path
from todos.views import TodoList_view

urlpatterns = [
    path("", TodoList_view, name="todo_list_list"),
]
