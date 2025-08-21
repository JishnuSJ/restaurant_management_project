from django.db import models

class UserProfile(Models.Model):
    user = models.OnetoOneField(USer,on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}({self.user.username})"