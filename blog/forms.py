from django import forms
from .models import *
from django import forms
from django.forms import ModelForm
from django.utils import timezone


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


#----------------------------


from .models import GeeksModel


# creating a form
class GeeksForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = GeeksModel

        # specify fields to be used
        fields = [
            "title",
            "description",
        ]
