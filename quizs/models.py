from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile
from Category.models import Category

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    question_slug = models.CharField(max_length=200,unique=True)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question
    
class solve_question(models.Model):
    ques = models.ForeignKey(Question, on_delete=models.CASCADE)
    solver = models.ForeignKey(User, on_delete=models.CASCADE)
    
class choice(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    

