from django.contrib                 import messages
from django.shortcuts               import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms  import UserCreationForm, UserChangeForm
from forms import *

# Create your views here.
def index( request ):
    dict = { 'page' : 'index' }
    return render( request, "index.html", dict )

def about( request ):
    dict = { 'page' : 'about' }
    return render( request, "about.html", dict )

def signup( request ):
    if request.method == 'POST':
        signupForm = UserSignupForm( request.POST )
        if signupForm.is_valid():
            user           = signupForm.save( commit = False )
            user.is_active = True # set to false for email verification
            user.save()
            messages.success( request, 'Registration succesfully completed.' )
            return redirect( 'login' )
    else:
        signupForm = UserSignupForm()

    dict = { 'page' : 'signup', 'signupForm' : signupForm }
    
    return render( request, 'signup.html', dict )

@login_required
def dashboard( request ):
    dict = { 'page' : 'dashboard' }
    return render( request, 'dashboard.html', dict )

@login_required
def settings( request ):
    prefill = { 'email' : request.user.email, 'first_name' : request.user.first_name, 'last_name' : request.user.last_name }
    
    if request.method == 'POST':
        userChangeForm = UserAccountSettings( request.POST, instance = request.user )
        if userChangeForm.is_valid():
            userChangeForm.save()
            messages.success( request, 'Profile updated!' )
    else:
        userChangeForm = UserAccountSettings( initial = prefill )
    dict = { 'page' : 'settings', 'userChangeForm' : userChangeForm }
    return render( request, 'settings.html', dict )

