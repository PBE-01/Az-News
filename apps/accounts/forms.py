from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email"
            }
        )
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password"
            }
        )
    )

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm PASsword', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password do not match. ")