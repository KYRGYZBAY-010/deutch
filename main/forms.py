from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-input', 'placeholder': 'exemple@gmail.com'}))
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-input', 'placeholder':'XXXX XXXX'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-input', 'placeholder':'XXXX XXXX'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-input', 'placeholder': 'Username'}))

    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


#password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'input', 'placeholder':'XXXX XXXX'}))
#