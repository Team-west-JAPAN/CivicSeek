from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.conf import settings
from django.contrib.auth import get_user_model
from django import forms
from accounts.models import Profile

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    '''
    UserCreationFormのサブクラス
    '''
    class Meta:
        model = UserModel
        # fields = ('name', 'birth_data', 'email', 'password','region','profession')
        fields = ('username', 'email', 'password1', 'password2')


class CustomLoginForm(AuthenticationForm):
    '''login用のform
    '''
    username = forms.EmailField(label='Email')


class ProfileEditForm(forms.ModelForm):
    '''profileを編集するためのform
    !!!: このformはまだサニタイジング処理を記述されていないため、メソッドをオーバーライドしてサニタイジングする必要がある
    '''
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'is_student', 'birth_date')


class CusomUserChangeForm(UserChangeForm):
    '''UserChangeFormのサブクラス
    '''
    class Meta:
        model = UserModel
        fields = ('username', 'email')
