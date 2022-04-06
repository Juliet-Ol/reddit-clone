from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm 
from .models import Post, Profile
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request,'redditclone/index.html')


# User registration 


def register(request):
    form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User has been registered')

            return redirect ('/accounts/login')
        else:
            return render(request, 'registration/registration_form.html', {'form': form})

    else:
        return render(request, 'registration/registration_form.html', {'form': form})


def editProfile(request):
    form = ProfileForm(initial={'name':request.user.username, 'bio':'test'})

   
    return render(request, 'profile/edit.html', {'form': form})  



def profile(request):
    form = ProfileForm

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        Profile.objects.filter(id__gt=1)
        
        profile=Profile.objects.get(author= request.user.id)
       
        if form.is_valid():
            avatar=form.cleaned_data['avatar']   
            name=form.cleaned_data['name']  
            bio=form.cleaned_data['bio'] 
            author=request.user            
            profile=Profile(avatar,name,bio,author)
            form.save()

            profile=Profile.objects.get(author= request.user.id)
            messages.success(request, 'Profile has been updated')

            return redirect ('/profile')
        else:
            return render(request, 'profile/edit.html', {'form': form})

    else:
        profile=Profile.objects.get(author= request.user)

        return render(request, 'profile/show.html', {'form': form, 'profile':profile})       
        




