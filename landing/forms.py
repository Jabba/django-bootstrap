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
        
class UserAccountSettings( forms.ModelForm ):
    class Meta:
        model   = User
        exclude = ( "username", "is_superuser", "last_login", 
                    "is_staff", "is_active", "date_joined", 
                    "password", "groups", "user_permissions" )

    def save( self ):
        user = super( UserAccountSettings, self ).save()