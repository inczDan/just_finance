from django.contrib.auth.models import User, AbstractUser
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    avatar = models.URLField(max_length=1024, null=True, blank=True)
    def __str__(self):
        return str(self.user)



# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=100)
