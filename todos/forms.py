from django.forms import ModelForm
from todos.models import TodoList


class TodoForm(ModelForm):
    class Meta:
        model = TodoList
        fields = [
            "name",
        ]
