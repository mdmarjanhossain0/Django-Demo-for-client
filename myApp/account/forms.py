from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import Account


class RegistrationForm(UserCreationForm):
	email=forms.EmailField(max_length=61,help_text="Required. Add a vaild email Address")



	class Meta:
		model=Account
		fields=('email','username','password1','password2')



class AccountAuthenticationForm(forms.ModelForm):

	password= forms.CharField(label="password",widget=forms.PasswordInput)


	class Meta:
		model=Account
		fields=('email','password')


	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email,password=password):
				raise forms.ValidationError("Invalid Login")



class AccountUpdateForm(forms.ModelForm):

	class Meta:
		model = Account
		fields = ('email','username', 'profile_picture')

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email

		raise forms.ValidationError('Email "%s" is already used.'%email)



	def clean_username(self):
		username= self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username

		raise forms.ValidationError('User Name "%s" is already used.'%username)