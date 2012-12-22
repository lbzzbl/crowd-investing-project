from django.db import models
from django.forms import ModelForm

from datetime import datetime

INVESTMENT_CHOICES = (
    ('100', '$100'),
    ('250', '$250'),
    ('500', '$500'),
    ('1000', '$1000'),
    ('2000', '$2000'),
    ('3000', '$3000'),
    ('4000', '$4000'),
    ("5000", '$5000'),
)

class User(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    amount = models.IntegerField(choices=INVESTMENT_CHOICES, default=None)
    reg_date = models.DateTimeField(default=datetime.now())

class RegistrationForm(ModelForm):
    class Meta:
        model = User