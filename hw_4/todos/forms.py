from django import forms
from .models import TodoList, Todo

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description']

class TodoForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
