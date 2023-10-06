from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir Contraseña'
            }
        )
    )



    class Meta:
        model = User
        fields =(
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2','Las contraseñas no son iguales.')


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username:',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'style':'{margin: 10px}',
            }
        )
    )
    password = forms.CharField(
        label='Password:',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña'
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm,self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos.')
        
        return self.cleaned_data
    
class UpdatePasswordForm(forms.Form):
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Contraseña Nueva'
            }
        )
    )

class VerificationForm(forms.Form):
    coderegistro = forms.CharField(required=True)

    def __init__(self,pk,*args,**kwargs):
        self.id_user = pk
        super(VerificationForm,self).__init__(*args,**kwargs)

    def clean_coderegistro(self):
        codigo = self.cleaned_data['codigoregistro']

        if len(codigo) == 6:
            activo = User.objects.code_validation(
                self.id_user,
                codigo
            )
            if not activo:
                raise forms.ValidationError('El codigo es incorrecto.')
        else:
            raise forms.ValidationError('El codigo es incorrecto.')