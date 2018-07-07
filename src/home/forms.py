from django import forms
from .models import Image
from .models import Parts
# from .validators import validate_category


class PostPartCreateForm(forms.ModelForm):

    class Meta:
        model = Parts
        fields = [
            'name',
            'category',
            'manufacturer',
            'modelName',
            'manufacturingYear',
            'usedDuration',
            'description',
            'images',
        ]

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields= ["name", "imageFile"]

# class SignUpForm(forms.ModelForm):
#     fullname =         forms.CharField(max_length=30, required=True, help_text='Full name.')
#     address =          forms.CharField(max_length=255, required=True, help_text='House number and street')
#     city =             forms.CharField(max_length=30, required=True, help_text='XYZ.')
#     postalcode =       forms.CharField(max_length=10, required=True, help_text='XYZ.')
#     country =          forms.CharField(max_length=30, required=True, help_text='XYZ.')
#     mobilenumber =     forms.DecimalField(max_digits=10, required=True, help_text='XYZ.')
#     email =            forms.EmailField(max_length=255, help_text='Required. Inform a valid email address.')
#
#     class Meta:
#         model = User
#         fields = ('fullname','username', 'email', 'password1', 'password2','address','city','postalcode','country','mobilenumber' )
#
#     def clean_username(self):
#         username=self.cleaned_data['username']
#         if User.objects.filter(username).exists():
#             raise forms.ValidationError(_("This username already exists."))
#         return cleaned_data