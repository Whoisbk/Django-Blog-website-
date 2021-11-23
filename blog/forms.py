from django import forms


class SigninUser(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'30',
        'title':'name',
        'placeholder':'Username'}))
    pass1 = forms.CharField(required=False,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'size':'30',
        'placeholder':'Password'}))

class CreateUser(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Username'}))
    fname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'First Name'}))
    lname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Last Name'}))
    email = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Email'}))
    pass1 = forms.CharField(required=False,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'size':'50',
        'placeholder':'Password'}))
    pass2 = forms.CharField(required=False,max_length=32,label="",widget=forms.PasswordInput(
        attrs={'size':'50',
        'placeholder':'Confirm Password'}))

class CreatePost(forms.Form):
    title = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'60',
        'placeholder':'Title'}))
    content = forms.CharField(required=False,label="",widget=forms.Textarea(
        attrs={'size':'10',
        'placeholder':'Content Here'}))
  

class EditUser(forms.Form):
    username = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Username'}))
    fname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'First Name'}))
    lname = forms.CharField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Last Name'}))
    
    email = forms.EmailField(required=False,max_length=200,label="",widget=forms.TextInput(
        attrs={'size':'50',
        'placeholder':'Email'}))
    