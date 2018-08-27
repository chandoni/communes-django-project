from django import forms

class BulletinForm(forms.Form):
    title = forms.CharField(max_length=64)
    caption = forms.CharField(max_length=128)
    
