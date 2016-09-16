from .models import *
from django import forms


class addImgAlbum(forms.Form):
    imagen = forms.ImageField()
