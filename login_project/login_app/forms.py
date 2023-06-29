from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, NewsModel, UserModel

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


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

	class Meta:
		model = User
		fields = ('email','first_name','last_name', 'password1', 'password2', )

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = User.objects.exclude(pk=self.instance.pk).get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email:%s is already in use.' % account.email)

class NewsForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = NewsModel
 
        # specify fields to be used
        fields = [
            "title",
            "content",
            "author",
            "tags",
            "core_categories",
        ]