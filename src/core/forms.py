from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.db.models.signals import pre_save, post_save
# from .validators import validate_category
from django.conf import settings
# User = settings.AUTH_USER_MODEL

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('bio', 'location', 'birth_date')

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active or not user.is_validated:
            raise forms.ValidationError('There was a problem with your login.', code='invalid_login')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            print('Sorry, that login was invalid. Please try again.')
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class SignUpForm(UserCreationForm):
    fullname =         forms.CharField(max_length=30, required=True, help_text='Full name.')
    address =          forms.CharField(max_length=255, required=True, help_text='House number and street')
    city =             forms.CharField(max_length=30, required=True, help_text='XYZ.')
    postalcode =       forms.CharField(max_length=10, required=True, help_text='XYZ.')
    country =          forms.CharField(max_length=30, required=True, help_text='XYZ.')
    mobilenumber =     forms.DecimalField(max_digits=10, required=True, help_text='XYZ.')
    email =            forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('fullname', 'username', 'email', 'password1', 'password2', 'address', 'city', 'postalcode', 'country', 'mobilenumber' )

    # def clean_username(self):
    #     username=self.cleaned_data['username']
    #     if User.objects.filter(username).exists():
    #         raise forms.ValidationError(_("This username already exists."))
    #     return cleaned_data
    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.profile.fullname = form.cleaned_data['fullname']
    #     if commit:
    #         user.save()

    #     return user
# class UserCreateForm(forms.ModelForm):
#     class  Meta:
#         model = User
        # fields = [
        #     'name',
        #     'location',
        #     'catergory',
        #     ]
