from django import forms
from .models import ResumeModel

class NameForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='',
                                 widget=forms.TextInput({'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=50, label='',
                                widget=forms.TextInput({'placeholder': 'Last Name'}))


class EmailForm(forms.Form):    
    email = forms.EmailField(max_length=100, label='',
                             widget=forms.TextInput({'placeholder': 'Email Address'}))
    

class UploadForm(forms.ModelForm):
    
    class Meta:
        model = ResumeModel
        fields = '__all__'


class JobSearchForm(forms.Form):
    job_description = forms.CharField(max_length=50, label='',
                                      widget=forms.TextInput({'placeholder': 'Job Description'}))
    job_location = forms.CharField(max_length=50, label='',
                                   widget=forms.TextInput({'placeholder': 'Job Location'}))
