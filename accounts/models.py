from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users')
    Quiz_author = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class User_details(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    number_prob_solve = models.IntegerField(default=0) 
    accurate = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    accuracy = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f"User Details for {self.username.username}"