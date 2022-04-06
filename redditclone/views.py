from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

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
        




