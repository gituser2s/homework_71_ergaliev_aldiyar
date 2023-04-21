from django import forms
from django.contrib.auth import get_user_model
from accounts.models import Account


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)


class CustomUserCreationForm(forms.ModelForm):
    gender_choice = (('Мужской', 'Мужской'), ('Женский', 'Женский'))
    username = forms.CharField(label='Логин', required=True)
    email = forms.EmailField(label="Почта", required=True)
    avatar = forms.ImageField(label="Аватар", required=False)
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)
    name = forms.CharField(label='Имя', required=False)
    information = forms.CharField(label="Информация", required=False, widget=forms.Textarea)
    phone = forms.IntegerField(label="Номер", required=False)
    gender = forms.ChoiceField(choices=gender_choice, label='Пол')

    class Meta:
        model = get_user_model()
        fields = ('username', 'email',  'avatar', 'password', 'password_confirm', 'name', 'information', 'phone', 'gender')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'avatar', 'email', 'information', 'name', 'phone', 'gender')
        labels = {'username': 'Логин', 'email': 'Почта', 'avatar': 'Аватар', 'phone': 'Номер', 'gender': 'Пол'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('username', 'avatar', 'email', 'information', 'name', 'phone', 'gender')
        labels = {'username': 'Логин', 'email': 'Почта', 'avatar': 'Аватар', 'phone': 'Номер', 'gender': 'Пол'}
