from django.shortcuts               import render, redirect
from django.template                import Context
from django.contrib.auth.decorators import login_required

# Create your views here.
def index( request ):
    dict = { 'page' : 'index' }
    return render( request, "index.html", dict )

def about( request ):
    dict = { 'page' : 'about' }
    return render( request, "about.html", dict )

def signup( request ):
    dict = { 'page' : 'signup' }
    return render( request, "signup.html", dict )

def dashboard( request ):
    dict = { 'page' : 'dashboard' }
    return render( request, "dashboard.html", dict )
