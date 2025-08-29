from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name','email']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'yourname'}),
            'email':forms.EmailInput(attrs={'placeholder':'your email'})
        }
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if not email or '@'not in email:
                raise forms.validationError("please enter valid email")
            return email