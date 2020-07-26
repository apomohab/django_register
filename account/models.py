from django.db import models

# Create your models here.

#add the prifile user

from django.conf import settings

class profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%y/%m/%d', blank=True)

    def __str__(self):
        return f'profile for user {self.user.username}'
