from django import forms

from .models import Answer, Free_Board

class FreeForm(forms.ModelForm):
    class Meta:
        model = Free_Board
        fields = ['b_title', 'b_content']
        labels = {
            'b_title':'제목',
            'b_content':'내용'
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content':'내용'
        }