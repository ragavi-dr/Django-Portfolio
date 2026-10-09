from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name','email', 'message']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-contrl mb-3'}),
            'email' : forms.EmailInput(attrs={'class':'form-control mb-3'}),
            'message' : forms.Textarea(attrs={'class' : 'form-control mb-3', 'rows':4}),
        }