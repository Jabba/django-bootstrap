from django                     import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm, UserChangeForm

class UserSignupForm( UserCreationForm ):
    class Meta:
        model  = User
        fields = ( "username", "email", "password1", "password2" )

    def save( self, commit = True ):
        user = super( UserSignupForm, self ).save( commit = False )
        user.email      = self.cleaned_data[ "email" ]
        user.save()
        return user
        
class UserAccountSettings( UserChangeForm ):
    class Meta:
        model  = User
        fields = ( "email", "password" )

    def save( self ):
        user         = super( UserCreationForm, self ).save()
        user.email   = self.cleaned_data[ "email" ]
        user.save()
        return user