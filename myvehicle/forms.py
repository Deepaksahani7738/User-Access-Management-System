from django import forms
from .models import Management_Data
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class mydata(forms.ModelForm):
    class Meta:
        model = Management_Data
        fields =['user','vehicle_number','vehicle_type','vehicle_model','vehicle_desc']
        widgets = { 
                   'vehicle_number':forms.TextInput(attrs={'class':'form-control','style':'max-width:800px','placeholder':'Enter vehicle number'}),
                    'vehicle_model':forms.Textarea(attrs={'class':'form-control','style':'max-width:800px','placeholder':'Enter model Number'}),
                    'vehicle_desc':forms.Textarea(attrs={'class':'form-control','style':'max-width:800px','placeholder':'Enter description'}),

                   }
        
class PostBlogForm(forms.ModelForm):
    class Meta:
        model = Management_Data
        fields = ['vehicle_number','vehicle_model','vehicle_desc']
        widgets = { 
                   'vehicle_number':forms.TextInput(attrs={'class':'form-control','style':'max-width:500px','placeholder':'Enter vehicle number'}),
                    'vehicle_model':forms.Textarea(attrs={'class':'form-control','style':'max-width:500px','placeholder':'Enter model Number'}),
                    'vehicle_desc':forms.Textarea(attrs={'class':'form-control','style':'max-width:500px','placeholder':'Enter description'}),

                   }
        
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password1','password2')
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','style':'max-width:1000px','placeholder':'Enter Your Email'}))
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','style':'max-width:600px','placeholder':'Enter Your FirstName'}))
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','style':'max-width:600px','placeholder':'Enter Your Lastname'}))
    username = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','style':'max-width:1000px','placeholder':'Enter Your Usename'}))
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','style':'max-width:600px','placeholder':'Enter Your password'}))
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','style':'max-width:600px','placeholder':'Enter Your Confirm password'}))
    check = forms.BooleanField(required=True)