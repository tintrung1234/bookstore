from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomerUser(AbstractUser):
    phone_number = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=255, default='')
    # birthdate = models.DateField(default='')
    gender = models.BooleanField(default=True)
    # image = models.CharField(max_length=255, default='')
