from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

# Helper function to create widget with common attributes
def custom_widget(placeholder, css_class="form-control"):
    return forms.TextInput(attrs={'class': css_class, 'placeholder': placeholder})

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=custom_widget('Email Address'))
    first_name = forms.CharField(label="", max_length=100, widget=custom_widget('First Name'))
    last_name = forms.CharField(label="", max_length=100, widget=custom_widget('Last Name'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget = custom_widget('User Name')
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted">'
            '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'
            '</span>'
        )

        self.fields['password1'].widget = custom_widget('Password')
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>Your password can\'t be too similar to your other personal information.</li>'
            '<li>Your password must contain at least 8 characters.</li>'
            '<li>Your password can\'t be a commonly used password.</li>'
            '<li>Your password can\'t be entirely numeric.</li>'
            '</ul>'
        )

        self.fields['password2'].widget = custom_widget('Confirm Password')
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        )

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=custom_widget("First Name"), label="")
    last_name = forms.CharField(required=True, widget=custom_widget("Last Name"), label="")
    email = forms.CharField(required=True, widget=custom_widget("Email"), label="")
    phone = forms.CharField(required=True, widget=custom_widget("Phone"), label="")
    address = forms.CharField(required=True, widget=custom_widget("Address"), label="")
    city = forms.CharField(required=True, widget=custom_widget("City"), label="")
    state = forms.CharField(required=True, widget=custom_widget("State"), label="")
    zipcode = forms.CharField(required=True, widget=custom_widget("Zipcode"), label="")

    class Meta:
        model = Record
        exclude = ("user", )
