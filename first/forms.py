
from django import forms
from .models import Register
from .models import LOTP

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Register
        db_table = 'register'
        fields = [
            'username',
              'email',
              'password'
            ]
class SignInForm(forms.ModelForm):
    class Meta:
        model = LOTP
        db_table = 'LOTP'
        fields = [
            'otpL'
            ]