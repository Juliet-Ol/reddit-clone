from cProfile import Profile
from pyexpat import model
from django import forms
from .models import Profile, Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['author']
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  
        exclude = ['author']      