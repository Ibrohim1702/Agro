from django import forms

from appAgro.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
