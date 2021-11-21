import urllib.parse
from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from . import models


def validate_website_url(website):
    """Validate website into valid URL"""
    msg = "Cannot validate this link: %s" % website
    validate = URLValidator(message=msg)
    try:
        validate(website)
    except:
        # o = urllib.parse.urlparse(website)
        # if o.path:
        #     path = o.path
        #     while path.endswith('/'):
        #         path = path[:-1]
        #     path = "http://"+path
        #     validate(path)
        #     return path
        # else:
        raise ValidationError(message=msg)
    return website 


class PersonFrom(forms.ModelForm):
    url = forms.CharField(validators=[URLValidator])

    class Meta:
        model = models.Person
        fields = (
            'first_name',
            'last_name',
            'address',
            'phone',
            'url'
        )

    def clean_url(self):
        url = self.cleaned_data.get('url', False)
        return validate_website_url(url)
