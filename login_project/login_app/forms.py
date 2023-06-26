from django import forms
from .models import UserModel

class UserForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = UserModel
 
        # specify fields to be used
        fields = [
            "name",
            "emailId",
            "password",
            "id",
        ]
    # username = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100, widget=forms.PasswordInput)
