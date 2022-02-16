from django import forms
from .models import Customer, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


def min_length_2_validator(value):
    if len(value) < 2:
        # ValidatorError 예외 강제로 발생시킴
        raise forms.ValidationError('이름은 2글자 이상 입력해주세요!')


#  Form 클래스
class CustomerForm(forms.Form):
    name = forms.CharField(validators=[min_length_2_validator])
    email = forms.EmailField()
    birthdate = forms.DateField()
    choice = [('1', '남자'), ('0', '여자')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=choice)


# Modelform 상속받는 CustomerModelForm 클래스 정의
class CustomerModelForm(forms.ModelForm):
    choice = [('1', '남자'), ('0', '여자')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=choice)

    class Meta:
        model = Customer
        fields = ('name', 'email', 'birthdate', 'gender',)
        # fields = ['name', 'email', 'birthdate', 'gender']
