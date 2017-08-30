from django import forms
from django.contrib.auth.models import User
from .models import Student,Professor


#from .models import Post
class UploadFileForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class StudentForm(forms.ModelForm):
    name = forms.CharField(label='Your name', max_length=20)
    gender = forms.CharField(label='Gender' , max_length=20)
    mobileno = forms.CharField(label='Mobile No' , max_length=20)
    year = forms.CharField(label='Year' , max_length=20)
    div = forms.CharField(label='Division' , max_length=20)
    sap = forms.CharField(label='SAP ID' , max_length=20)
    email = forms.CharField(label='Email ID' , max_length=20)
    password = forms.CharField(label='Password' , max_length=20)
    class Meta:
        model = Student
        fields = '__all__'

class StudentLoginForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Password' , max_length=20)

class ProfessorForm(forms.ModelForm):
    name = forms.CharField(label='Your name', max_length=20)
    gender = forms.CharField(label='Gender', max_length=20)
    mobileno = forms.CharField(label='Mobile No', max_length=20)
    dept = forms.CharField(label='Department', max_length=20)
    sap = forms.CharField(label='SAP ID', max_length=20)
    email = forms.CharField(label='Email ID', max_length=20)
    password = forms.CharField(label='Password', max_length=20)
    class Meta:
        model = Professor
        fields = '__all__'

class ProfessorLoginForm(forms.Form):
	name = forms.CharField(label='Your name', max_length=20)
	password = forms.CharField(label='Password', max_length=20)

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields=['email','password']

