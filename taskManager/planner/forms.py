from .models import Task
from django.forms import ModelForm, TextInput, DateInput, TimeInput, Textarea

class DateInp(DateInput):
    input_type = 'date'

class TasksForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'announce', 'date', 'time', 'description']

        class_for_widgets = 'form-control form-control-lg'

        widgets = {
            "title": TextInput(attrs={
                'class': class_for_widgets,
                'placeholder': 'Название'
            }),
            "announce": TextInput(attrs={
                'class': class_for_widgets,
                'placeholder': 'Заголовок'
            }),
            "date": DateInp(attrs={
                'class': class_for_widgets,
                'type': 'date',
            }),
            "time": TimeInput(attrs={
                'class': class_for_widgets,
                'type': 'time',
            }),
            "description": Textarea(attrs={
                'class': class_for_widgets,
                'placeholder': 'Описание'
            }),
        }