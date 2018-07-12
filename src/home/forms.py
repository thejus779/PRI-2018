from django import forms
from .models import Image
from .models import Parts, PartsRequest, Contact
from .models import Query
from django.forms.widgets import NumberInput
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
            'city',
            'country',
            'zipcode',
        ]

class PartRequestCreateForm(forms.ModelForm):

    class Meta:
        model = PartsRequest
        fields = [
            'name',
            'category',
            'manufacturer',
            'modelName',
            'manufacturingYear',
            'usedDuration',
            'city',
            'country',
            'zipcode',
        ]

class ContactCreateForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
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

class QueryCaseBaseForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ("category", "make", "country", "manufacturer",
                 "manufacturerYear",
                  "city", "zipCode", "usedDuration")

        widgets = {
            # 'visualQualityRating': NumberInput (attrs={'type': 'range', 'step': '1', 'max': '10', 'min': '1',
            #                                              'value': '5', 'oninput': 'visualOutput.value=this.value'}),
            'manufacturerYear': NumberInput (attrs={'type': 'range', 'step': '1', 'max': '10', 'min': '1',
                                                       'value': '5', 'oninput': 'yearOutput.value=this.value'}),
            'zipCode': NumberInput (attrs={'type': 'range', 'step': '1', 'max': '10', 'min': '1',
                                                            'value': '5',
                                                            'oninput': 'zipOutput.value=this.value'}),
            'usedDuration': NumberInput (attrs={'type': 'range', 'step': '1', 'max': '10', 'min': '1',
                                                          'value': '5', 'oninput': 'usedDOutput.value=this.value'}),

        }

    def __init__(self, *args, **kwargs):
        super(QueryCaseBaseForm, self).__init__(*args, **kwargs)
        self.fields["category"].required = False
        self.fields["make"].required = False
        # self.fields["continent"].required = False
        self.fields["country"].required = False
        self.fields["manufacturer"].required = False
        # self.fields["language"].required = False
        # self.fields["visualQualityRating"].required = False
        self.fields["manufacturerYear"].required = False
        self.fields["city"].required = False
        self.fields["zipCode"].required = False
        self.fields["usedDuration"].required = False