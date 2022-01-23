from django import forms

class PostForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", max_length=100)
    content = forms.CharField(label="Content",widget=forms.Textarea)