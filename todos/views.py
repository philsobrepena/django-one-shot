from django.shortcuts import render, get_object_or_404, redirect
from todos.models import TodoList, TodoItem
from todos.forms import TodoForm


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


def TodoList_Create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todolist = form.save()
            return redirect("todo_list_list")
    else:
        form = TodoForm()
    context = {"form": form}

    return render(request, "todos/create.html", context)
