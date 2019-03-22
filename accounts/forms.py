from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='Kullanıcı Adı')
    password = forms.CharField(max_length=50, label='Parola', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı adını ya da parolayı yanlış girdiniz.')
        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label='Kullanıcı Adı')
    password = forms.CharField(max_length=50, label='Parola', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, label='Parola Doğrulama', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2'
        ]

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('passwor2')
        if password and password2 and password != password2:
            raise forms.ValidationError('Parolalar eşleşmiyor.')
        return password2