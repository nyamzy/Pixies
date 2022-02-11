from django import forms
from pix.models import Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ["pub_date", "user"]
