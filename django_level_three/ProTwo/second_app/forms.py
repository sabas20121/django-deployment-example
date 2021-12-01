from django import forms
from django.core import validators
from django.db.models import fields
from second_app.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model =User
        fields = '__all__'
        



""" class FormName(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    verify_email = forms.EmailField(label='Type email again:')
    age = forms.IntegerField(max_value=60)
    comments = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email =  all_clean_data['email']
        vmail =  all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Email did not match. Type again:') """