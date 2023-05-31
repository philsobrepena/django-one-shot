from django.shortcuts import render, get_object_or_404
from todos.models import TodoList, TodoItem


# Create your views here.


def TodoList_view(request):
    todolist = TodoList.objects.all()
    context = {
        "todo_list": todolist,
    }
    return render(request, "todos/lists.html", context)


def TodoList_Details(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/details.html", context)
