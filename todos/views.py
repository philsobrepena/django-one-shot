from django.shortcuts import render
from todos.models import TodoList


# Create your views here.
def TodoList_view(request):
    todolist = TodoList.objects.all()
    context = {
        "todo_list": todolist,
    }
    return render(request, "todos/lists.html", context)
