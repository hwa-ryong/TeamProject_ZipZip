from django import forms

from .models import Review_Board, Answer_Review


class FreeForm(forms.ModelForm):
    class Meta:
        model = Review_Board
        fields = ['r_title', 'r_content', 'r_type']
        labels = {
            'r_title': '제목',
            'r_content': '내용',
            'r_type': '구분',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer_Review
        fields = ['content']
        labels = {
            'content': '내용'
        }
