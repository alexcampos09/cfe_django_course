from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=True)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=False)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["full_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split(".")
        if not extension == "br":
            raise forms.ValidationError("Tente um e-mail brasileiro")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        #write validation code
        return full_name
