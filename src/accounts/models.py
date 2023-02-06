from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=60)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.first_name + " " + self.last_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(default=None, upload_to='profiles/')
    dob = models.DateField(null=True,blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username
