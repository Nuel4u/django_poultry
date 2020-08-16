from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control" ,"placeholder":"your full name"}))
    age = forms.IntegerField(max_value=3)
    email =forms.EmailInput(attrs={"class":"form-control" ,"placeholder":" email address"})
    address = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control" ,
    "placeholder":"your full address"}))