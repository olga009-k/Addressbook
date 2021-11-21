from django.db import models
from django_base64field.fields import Base64Field

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    url = models.CharField(max_length=50)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='Full name')
        ]

    def __str__(self):
        return '%s %s %s %s' % (self.first_name, 
                                self.last_name, 
                                self.address, 
                                self.phone,
                                self.url)



