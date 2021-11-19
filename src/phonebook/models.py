from django.db import models

# Create your models here.


class Persone(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='Full name')
        ]

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.last_name, self.address)


    def all_phones_to_string(self):
        return ", ".join([phone.phone for phone in self.phones.all()])

class Phone(models.Model):
    phone = models.CharField("Phone", max_length=50)
    contact = models.ForeignKey(
        Persone, 
        on_delete=models.CASCADE,
        related_name="phones")

    def __str__(self):
        return self.phone

