from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, Select

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'priority']
        choice_priority = [
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
        ]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название дела',
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание дела',
                'rows': 3,
            }),
            'priority': Select(choices=choice_priority, attrs={
                'class': 'form-control',
                'placeholder': 'Приоритет дела',
            }),
        }

