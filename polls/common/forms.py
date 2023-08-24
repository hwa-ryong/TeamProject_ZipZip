
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.validators import ASCIIUsernameValidator


# 아이디 영어와 숫자만
class EnglishUsernameField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [ASCIIUsernameValidator()]
        kwargs['error_messages'] = {
            'invalid': '영어와 숫자만 입력 가능합니다.',
        }
        super().__init__(*args, **kwargs)

#회원가입 폼
class UserForm(UserCreationForm):
    last_name = forms.CharField(max_length=20, label='이름')
    email = forms.EmailField(label='이메일')
    username = EnglishUsernameField(label='아이디')

    class Meta:
        model = User
        fields = ['username', 'password1', 'last_name', 'email']

#사업자 회원가입 폼
class SignupForm(UserCreationForm):
    # 추가 필드 정의
    is_business = forms.BooleanField(label='사업자 여부', required=False)
    business_license = forms.FileField(label='사업자 등록증', required=False)
    last_name = forms.CharField(max_length=20, label='이름')
    email = forms.EmailField(label='이메일')
    username = EnglishUsernameField(label='아이디')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_business', 'business_license', 'email', 'last_name')

# 사용자 정보 업데이트 폼
class UserInformationUpdateForm(forms.ModelForm):
    last_name = forms.CharField(max_length=20, label='이름')
    email = forms.EmailField(label='이메일')

    class Meta:
        model = User
        fields = ['last_name', 'email']