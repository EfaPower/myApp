from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        # Call the parent's clean() method to initialize cleaned_data
        cleaned_data = super().clean()

        # Access the cleaned data safely
        username = cleaned_data.get('username')  # Ensure this is not misnamed
        password = cleaned_data.get('password')

        # Example validation
        if username and len(username) < 5:
            self.add_error('username', "Username must be at least 5 characters long.")

        return cleaned_data
         