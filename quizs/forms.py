from .models import Question,choice
from django import forms
from Category.models import Category


Choice = (
    ('5','5'),
    ('10','10'),
    ('15','15'),
)

class Make_Questions(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question' , 'option1', 'option2', 'option3', 'option4', 'answer','category',]


class Choice_Ques_type(forms.ModelForm):
    choice = forms.ChoiceField(choices=Choice)
    class Meta:
        model = choice
        fields = ['category','choice',]
     
        
        
