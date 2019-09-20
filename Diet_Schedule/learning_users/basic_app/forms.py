from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo,Video

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)

class VideoForm(forms.ModelForm):
    class Meta():
        model= Video
        fields= ["name", "videofile", 'desciption','categories', 'tags', 'reference_Id']
