from django import forms

from . import models

class PersonFrom(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = (
            'first_name',
            'last_name',
            'address',
            'phone'
        )


