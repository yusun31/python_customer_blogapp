from django import forms
from .models import Customer


def min_length_2_validator(value):
    if len(value) < 2:
        # ValidatorError 예외 강제로 발생시킴
        raise forms.ValidationError('이름은 2글자 이상 입력해주세요!')


#  Modelform 상속받는 CustomerModelForm 클래스 정의
class CustomerForm(forms.Form):
    name = forms.CharField(validators=[min_length_2_validator])
    email = forms.EmailField()
    birthdate = forms.DateField()
    choice = [('1', '남자'), ('0', '여자')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=choice)
