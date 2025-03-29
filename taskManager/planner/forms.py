from .models import Task
from django.forms import ModelForm, TextInput, DateInput, TimeInput, Textarea

class DateInp(DateInput):
    input_type = 'date'
class TasksForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'announce', 'date', 'time', 'description']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
            }),
            "announce": TextInput(attrs={
                'class': 'form-control',
            }),
            "date": DateInp(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            "time": TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
            }),
        }