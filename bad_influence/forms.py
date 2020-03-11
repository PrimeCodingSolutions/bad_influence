from .models import Player, Link
from django.forms import inlineformset_factory
from django import forms
from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['edge']

    edge = forms.BooleanField(widget=forms.CheckboxInput, required=False)


LinkFormset = inlineformset_factory(Player, Link,
                                    form=LinkForm,
                                    extra=0,
                                    can_delete=False,
                                    fk_name='source',
                                    fields=['edge'])



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):

     class Meta():
         model = UserProfileInfo
         fields = ('portfolio_site','profile_pic')