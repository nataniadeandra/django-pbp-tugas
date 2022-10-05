from todolist.models import Task
from django.forms import ModelForm, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
        )
        widgets = {
          'description': Textarea(attrs={'rows':5, 'cols':24}),
        }