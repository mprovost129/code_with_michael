from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


User = get_user_model()


class EmailOrUsernameAuthenticationForm(AuthenticationForm):
    username_field_label = 'Email or username'

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        self.fields['username'].label = self.username_field_label
        self.fields['username'].widget.attrs.update({
            'autofocus': True,
            'placeholder': self.username_field_label,
        })


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150, required=False)
    last_name = forms.CharField(max_length=150, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'email': 'Email address',
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'password1': 'Create a password',
            'password2': 'Confirm your password',
        }

        for field_name, placeholder in placeholders.items():
            self.fields[field_name].widget.attrs.update({'placeholder': placeholder})

        self.fields['username'].help_text = 'Keep it simple. This will be used later for community features like Q&A or chat.'
        self.fields['email'].help_text = 'You can use either your email or your username to sign in.'

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('An account with that email already exists.')
        return email

    def clean_username(self):
        username = self.cleaned_data['username'].strip()
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('That username is already taken.')
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        if commit:
            user.save()
        return user
